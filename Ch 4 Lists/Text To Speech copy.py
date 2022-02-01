# pip3 install gTTS pyttsx3 playsound


import gtts
from playsound import playsound
_n = input("enter Your Name")
tts = gtts.gTTS(_n)
tts.save("hello.mp3")
playsound("hello.mp3")