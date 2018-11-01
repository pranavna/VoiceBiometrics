#!/usr/bin/env python3

import speech_recognition as sr #using this for speech recognition
import pyttsx #allows for audio IO/OP
import hashlib #This package allows for hashing,
# get audio from the microphone

engine = pyttsx.init()
engine.say('Hi, Please authenticate yourself')
engine.runAndWait()


r = sr.Recognizer()
with sr.Microphone() as source: #using mic of the system
    print("Please clearly recite your passphrase")
    audio = r.listen(source) # get audio from the microphone

pwd = "55f55cb70c1c9e9f841992337c0a2a16"
#Used MD5 hashing. The password is moonlight!
speechd = r.recognize_google(audio)
#storing the audio signal as text. Using google API here.
pwdmd5 = hashlib.md5(speechd).hexdigest()
#converting the audio into text and hashing it
if pwdmd5 == pwd:
    print("Welcome User")
    engine.say('Hi user')
    engine.runAndWait()
else:
    print("Wrong Password")
    engine.say("you said")
    engine.say(speechd)
    engine.say('That is the wrong passphrase')
    engine.runAndWait()
