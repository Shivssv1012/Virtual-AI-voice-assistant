# import pyttsx3

# engine= pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
    
# import pyttsx3
# import threading
# import queue

# engine = pyttsx3.init()
# engine.setProperty('rate',170)



# # 🔹 Set properties ONCE
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)   # try 0 or 1
# engine.setProperty('rate', 170)             # speed (default ~200)
# engine.setProperty('volume', 1.0)           # 0.0 to 1.0

# def speak(text):
#     engine.stop()
#     print("Jarvis:", text)   # helpful for debugging
#     engine.say(text)
#     engine.runAndWait()
import winsound
import pyttsx3
import threading
import queue

engine = pyttsx3.init()
engine.setProperty('rate', 170)

speech_queue = queue.Queue()

def _speak_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

# start background thread
threading.Thread(target=_speak_worker, daemon=True).start()

def speak(text):
    print("Jarvis:", text)
    speech_queue.put(text)
    
def beep():
    winsound.Beep(1000, 300)