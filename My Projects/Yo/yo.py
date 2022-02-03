import pyttsx3
# import time
t = 0
# time.sleep(5)
while t < 1_00_000:
    t += 1
    engin = pyttsx3.init()
    voices = engin.getProperty('voices')
    engin.setProperty('voice', voices[2].id)
    engin.setProperty("rate", 400)
    engin.say(t)
    print(t)
    engin.runAndWait()