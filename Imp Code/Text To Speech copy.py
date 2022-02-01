# pip3 install gTTS pyttsx3 playsound

import gtts
from playsound import playsound
tts = gtts.gTTS(" Is bewkuf")
tts.save("hello.mp3")
playsound("hello.mp3")