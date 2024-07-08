#Install an external module and use it to perform an operation of your interest. 
import pyttsx3
engine = pyttsx3.init()
engine.say("Hi Man. How are you? I live in Bangladesh.")
engine.runAndWait()