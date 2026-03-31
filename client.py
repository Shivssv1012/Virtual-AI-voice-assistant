#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
from google import genai

def ask_jarvis(question):
    client=genai.Client(
       
       #add your api key here
    )
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="You are a virtual assistant Jarvis. Reply all responses in short and concise. {command}"
    )
    return response.text

print(ask_jarvis("what is coding"))
print(ask_jarvis("who is apj abdul kalam"))