from django.db import models
import uuid
import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from google.cloud import speech
from google.oauth2 import service_account
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import io
import subprocess

class MeetingCall(models.Model):
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
    attendees = models.JSONField()
    meeting_date = models.DateTimeField()
    meeting_topic = models.CharField(max_length=100)
    meeting_start_time = models.DateTimeField()
    meeting_end_time = models.DateTimeField()
    duration = models.DurationField()

    def save(self, *args, **kwargs):
        if not self.sys_id:
            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sys_id
    
class MeetingProtocol(models.Model):
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
    content = models.JSONField()
    meeting_call = models.ForeignKey(MeetingCall, on_delete=models.CASCADE, related_name='meeting_protocols')

    def save(self, *args, **kwargs):
        if not self.sys_id:
            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sys_id


class CallRecord(models.Model):
    timestamp = models.JSONField()
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
    call_id = models.CharField(max_length=50)
    caller_id = models.CharField(max_length=50)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    payload = models.FileField(upload_to='audio/')
    transcription = models.TextField()
    meeting_call = models.ForeignKey(MeetingCall, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.sys_id:
            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sys_id

    def transkribiere_audio(self):
        dateipfad = self.payload.path
        api_key_file = os.getenv('GOOGLE_API_KEY_PATH', r"C:\Entwicklung GI\unmoegliches_projekt\backend\openai\business-idea-427008-cbb158d6b32d.json")

        # Überprüfen, ob die JSON-Datei existiert
        if not os.path.isfile(api_key_file):
            raise FileNotFoundError(f"Die Datei {api_key_file} wurde nicht gefunden.")
        
        # Überprüfen, ob die Audiodatei im richtigen Format vorliegt
        try:
            audio = AudioSegment.from_file(dateipfad, format="wav")
        except CouldntDecodeError:
            # Datei konvertieren, wenn sie nicht im WAV-Format vorliegt
            wav_dateipfad = dateipfad.replace(".wav", "_converted.wav")
            self.konvertiere_datei(dateipfad, wav_dateipfad)
            audio = AudioSegment.from_file(wav_dateipfad, format="wav")

        audio = audio.set_channels(1)  # Konvertiere zu mono
        wav_dateipfad = dateipfad.replace(".wav", "_mono.wav")
        audio.export(wav_dateipfad, format="wav")
        
        # Ermitteln der Abtastrate der konvertierten Datei
        sample_rate = audio.frame_rate

        # Anmeldedaten laden
        credentials = service_account.Credentials.from_service_account_file(api_key_file)
        client = speech.SpeechClient(credentials=credentials)

        # Konvertierte Audiodatei laden
        with io.open(wav_dateipfad, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            language_code="de-DE",
        )

        # API Aufruf zur Transkription
        response = client.recognize(config=config, audio=audio)

        # Ergebnis speichern
        if response.results:
            self.transcription = response.results[0].alternatives[0].transcript
            self.save(update_fields=['transcription'])

    @staticmethod
    def konvertiere_datei(dateipfad, zielpfad):
        try:
            subprocess.check_call(['ffmpeg', '-i', dateipfad, zielpfad])
            print(f"Datei erfolgreich konvertiert: {zielpfad}")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Konvertierung der Datei: {e}")

@receiver(post_save, sender=CallRecord)
def transkribiere_audio_signal(sender, instance, created, **kwargs):
    if created:
        instance.transkribiere_audio()