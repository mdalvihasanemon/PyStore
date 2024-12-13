from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f"start {filename}")

text_to_speech("Hello, this is a Python utility script!")
