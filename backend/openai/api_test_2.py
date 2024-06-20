from google.cloud import speech
from google.oauth2 import service_account
from pydub import AudioSegment
import io
import os

def transkribiere_m4a_audio(dateipfad, api_key_file):
    # Überprüfen, ob die JSON-Datei existiert
    if not os.path.isfile(api_key_file):
        raise FileNotFoundError(f"Die Datei {api_key_file} wurde nicht gefunden.")
    
    # Konvertiere M4A in ein unterstütztes Format (z.B. WAV) und stelle sicher, dass es mono ist
    audio = AudioSegment.from_file(dateipfad, format="m4a")
    audio = audio.set_channels(1)  # Konvertiere zu mono
    wav_dateipfad = dateipfad.replace(".m4a", ".wav")
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

# Pfad zur API-Schlüssel-Datei und zur M4A-Test-Audiodatei
api_key_file = r"C:\Entwicklung GI\unmoegliches_projekt\backend\openai\business-idea-427008-cbb158d6b32d.json"
dateipfad = r"C:\Entwicklung GI\unmoegliches_projekt\backend\openai\Aufzeichnung.m4a"

transkribiere_m4a_audio(dateipfad, api_key_file)

