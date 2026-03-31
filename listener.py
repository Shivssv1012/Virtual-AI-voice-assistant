import speech_recognition as sr


# def listen():

#         try:
#                 r=sr.Recognizer()
#                 with sr.Microphone() as source:
#                         r.adjust_for_ambient_noise(source, duration=1)
#                         audio=r.listen(source,timeout=5,phrase_time_limit=4)
#                         command=r.recognize_google(audio)
#                         return command.lower()
#         except sr.UnknownValueError as e:
#                 print("couldn't understand audio ",e)
#                 return ""
#         except Exception as e:
#                 print("Error!")
#                 return ""
    
# def listen():
#     r = sr.Recognizer()
    
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         try:
#             audio = r.listen(source, timeout=5, phrase_time_limit=4)
#         except:
#             return ""

#     # mic released here

#     try:
#         return r.recognize_google(audio).lower()
#     except:
#         return ""
import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

WAKE_WORDS = ["jarvis", "jar vis", "service"]

# 🔹 Normal listening (for commands)
def listen():
    with mic as source:
        print("Listening for command...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""


# 🔹 Background callback (wake word detection)
def process_audio(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio).lower()
        print("Heard:", text)

        if any(word in text for word in WAKE_WORDS):
                print("wake word detected")
               # return wake word detected

    except:
        pass

    return None


# 🔹 Start background listening
def start_listening(callback):
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    def wrapper(recognizer, audio):
        result = process_audio(recognizer, audio)
        if result:
            callback(result)   # trigger main.py

    stop_listening = recognizer.listen_in_background(mic, wrapper)
    return stop_listening