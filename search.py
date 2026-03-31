import urllib.parse
import webbrowser
def google_search(query):
    query=urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
    