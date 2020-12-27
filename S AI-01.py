import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#here in avove line to change gender of voices[put 0 for male and 1 for female]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("welcome shivam") #here you can put your name or there that you want your assiastance to say at bignning
    speak("myself your AI") #same purpose as the above line of code
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speak(f"the current time is {time}")
    print('write below: \n')
    speak("write your question below")


time()

def wiki():
    question = input()
    result = wikipedia.summary(question)
    speak("according to wikipedia")
    print(result)
    speak(result)

wiki()
