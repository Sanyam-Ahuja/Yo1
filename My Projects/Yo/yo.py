import pyttsx3
import time
t = 0
time.sleep(10)
while t < 1_00_00000000:
    t += 1
    engin = pyttsx3.init()
    voices = engin.getProperty('voices')
    engin.setProperty('voice', voices[2].id)
    engin.setProperty("rate", 260)
    engin.say(t)
    engin.setProperty("rate", 240)
    engin.say("I will Make This Program Count Until Noticed By Mrbeast")
    print(t, "\nI will Make This Program Count Until Noticed By Mrbeast")
    engin.runAndWait()