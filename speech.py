import speech_recognition as sr
import time

def audio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      data = r.recognize_google(audio)
      print(data)
    return data   





