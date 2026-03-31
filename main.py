# import speech_recognition as sr
# import pyttsx3

import webbrowser
import pyaudio
from command.processcommad import processCommand
# import speech as sp
from speech import speak, beep
import requests 
            
import time
from listener import listen, start_listening

from config import WAKE_WORD



speak("Jarvis is online")

if __name__=="__main__":
    #sp.speak("Initializing jarvis...")
    print("Initializing jarvis....")


# 🔥 This runs when wake word is detected
def on_wake_word(text):
    print("WAKE WORD DETECTED:", text)

    beep()

    command = listen()

    if command:
        print("Command:", command)
        processCommand(command)
    else:
        print("No command detected")


# 🚀 Start system
print("Jarvis is always listening...")

stop = start_listening(on_wake_word)

# keep program alive
while True:
    time.sleep(0.5)
                
           
                    
         
         
            