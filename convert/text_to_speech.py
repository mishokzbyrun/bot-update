import gtts
import os

def text_to_speech(msg):
    tts = gtts.gTTS(msg, lang='en')
    audio_file = 'audio.mp3'
    tts.save(audio_file)
    if os.path.exists(audio_file):
        print("Audio was created successfully")
        return audio_file
    else:
        print("Failed to create audio file!")
        return None