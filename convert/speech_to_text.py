import speech_recognition as sr
from pydub import AudioSegment
import os

def ogg_to_wav(file):
    wfn = file.replace('.ogg', '.wav')
    segment = AudioSegment.from_file(file)
    segment.export(wfn, format='wav')
    return wfn 

def sp_to_text(file):
    recognizer = sr.Recognizer()
    audio_file = ogg_to_wav(file)
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google_cloud(audio_data)
            return f"Recognized speech: {text}"
        except sr.UnknownValueError:
            return "Speech recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from service; {e}"
