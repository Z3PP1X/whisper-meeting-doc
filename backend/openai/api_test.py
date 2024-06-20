from google.cloud import speech_v1p1beta1 as speech
import io

def transkribiere_audio(dateipfad, api_schluessel):
    client = speech.SpeechClient(credentials=api_schluessel)

    # Audiodatei laden
    with io.open(dateipfad, "rb") as audio_datei:
        content = audio_datei.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="de-DE",
    )

    # Audiodatei transkribieren
    response = client.recognize(config=config, audio=audio)

    # Transkription ausgeben
    for result in response.results:
        print("Transkript: {}".format(result.alternatives[0].transcript))

# Pfad zur Audiodatei
dateipfad = "C:\\Users\\Patri\\OneDrive\\Dokumente\\Audioaufzeichnungen\\Aufzeichnung.m4a"

# Ihr API-Schlüssel
api_schluessel = "AIzaSyB-F8ZRPesqQHJirvjgtyt7e8_qUpupSes"

transkribiere_audio(dateipfad, api_schluessel)
