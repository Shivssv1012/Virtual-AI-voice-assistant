import datetime
from listener import listen
from command.news import get_news
from command.search import google_search
import webbrowser
from config import WAKE_WORD
from .musicLibrary import music
from command.search import google_search
from speech import speak
from openai import OpenAI
from google import genai

def aiProcess(command):

    
    client=genai.Client(
        #add your api key here
        api_key="###"
    )
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="You are a virtual assistant Jarvis. Reply all responses in short and concise. {command}"
    )
    return response.text

   



def processCommand(c):
    print(f" command processed: {c}")
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com") 
    
    # elif c.lower().startswith("play"):
    #     song=c.lower().split(" ")[1]
    #     link=musicLibrary.music[song]
    #     webbrowser.open(link)
    elif c.lower().startswith("play"):
        parts=c.lower().split(" ")
        if len(parts)>1:
            song=parts[1]
            link=music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("song not found")
  #google searching
    elif "search" in c or "google" in c:
        query = c

        for word in ["search", "google", "for", "about"]:
            query = query.replace(word, "")

        query = query.strip()

        if not query:
            speak("What should I search?")
            query = listen()

        if query:
            speak(f"Searching for {query}")
            google_search(query)
        
    else:
        output=aiProcess(c)          
        speak(output)
   