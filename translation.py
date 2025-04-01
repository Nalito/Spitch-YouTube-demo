# Import modules
from spitch import Spitch
import os

# Instantiate a Spitch client
os.environ["SPITCH_API_KEY"] = os.getenv("Spitch")
client = Spitch()

# Get the input text, language, and voice
in_text = input("Enter the text: ")
in_lang = input("Enter the language code: ")
target_lang = input("Enter in the language you wish to translate to: ")

translation = client.text.translate(
    text=in_text,
    source=in_lang,
    target=target_lang,
)
print(translation.text)