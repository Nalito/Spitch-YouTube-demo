# Import modules
from spitch import Spitch
import os

# Instantiate a Spitch client
os.environ["SPITCH_API_KEY"] = os.getenv("Spitch")
client = Spitch()

# Get the input text, language, and voice
in_text = input("Enter the text: ")
in_lang = input("Enter the language code: ")
in_voice = input("Enter your preferred voice: ")

# Generate the audio file
with open("genAudio 2.wav", "wb") as f:
    response = client.speech.generate(
        text=in_text,
        language=in_lang,
        voice=in_voice
    )
    f.write(response.read())