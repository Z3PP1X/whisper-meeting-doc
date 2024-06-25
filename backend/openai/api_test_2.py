from google.cloud import speech
from google.oauth2 import service_account
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError  # Import the CouldntDecodeError class
import io
import os
import subprocess

def konvertiere_datei(dateipfad, zielpfad):
    try:
        subprocess.check_call(['ffmpeg', '-i', dateipfad, zielpfad])
        print(f"Datei erfolgreich konvertiert: {zielpfad}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Konvertierung der Datei: {e}")

def transkribiere_audio(dateipfad, api_key_file):
    # Überprüfen, ob die JSON-Datei existiert
    if not os.path.isfile(api_key_file):
        raise FileNotFoundError(f"Die Datei {api_key_file} wurde nicht gefunden.")
    
    # Überprüfen, ob die Audiodatei im richtigen Format vorliegt
    try:
        audio = AudioSegment.from_file(dateipfad, format="wav")
    except CouldntDecodeError:
        # Datei konvertieren, wenn sie nicht im WAV-Format vorliegt
        wav_dateipfad = dateipfad.replace(".wav", "_converted.wav")
        konvertiere_datei(dateipfad, wav_dateipfad)
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
        sample_rate_hertz=sample_rate,  # Verwenden Sie die tatsächliche Abtastrate der Datei
        language_code="de-DE",
    )

    # API Aufruf zur Transkription
    response = client.recognize(config=config, audio=audio)

    # Ergebnis anzeigen
    for result in response.results:
        print("Transkript: {}".format(result.alternatives[0].transcript))

# Pfad zur API-Schlüssel-Datei und zur Audiodatei
api_key_file = r"C:\Entwicklung GI\unmoegliches_projekt\backend\openai\business-idea-427008-cbb158d6b32d.json"
dateipfad = r"C:\Entwicklung GI\unmoegliches_projekt\backend\meeting_transcript\media\audio\audio.wav"

transkribiere_audio(dateipfad, api_key_file)
