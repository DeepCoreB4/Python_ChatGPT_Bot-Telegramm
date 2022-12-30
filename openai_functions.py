import os
import openai

# Verbindung zur OpenAI-API herstellen und ChatGPT-Modell angeben
# Verwendet den Wert der Umgebungsvariablen "OPENAI_API_KEY"
openai.api_key = os.environ.get("OPENAI_API_KEY")

model_engine = "chatgpt"

# Funktion, die ChatGPT verwendet, um auf eine Nachricht zu antworten
def generate_response(text):
    prompt = (f"User: {text}\n"
             f"MicroBot: ")
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    message = completions.choices[0].text
    return message.strip()
