import pyttsx3 
import datetime
import speech_recognition as sr
from word2number import w2n

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello. And welcome Los Pollos Hermanos family. My name is Gustavo but you can call me Gus")    
wishMe()

speak("Say a positive integer")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query
query = takeCommand().lower()

try:
    res = w2n.word_to_num(query)
except ValueError:
    res = int(input(">>>"))

m=[]

c=3

if res==1:
    speak("no need for cutting")
    print("No need for cutting")
    
elif res==2:
    speak("1st or 2nd ring")
    print("1st or 2nd ring")
    
elif res>=3:
    while res>=c:
        m.append(c)
        c=(c+1)*2
    speak(f"should have been cut in {len(m)} places")
    print("Should have been cut in", len(m), "places")
    speak("should be cut from the sagging places ")
    speak(m)
    print("Should be cut from the sagging places:",*m)
    
else:
    speak("That is not correct")
    print("That is not correct")

speak("Bye bye")
print("Bye")