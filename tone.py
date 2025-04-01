# Import modules
from spitch import Spitch
import os

# Instantiate a Spitch client
os.environ["SPITCH_API_KEY"] = os.getenv("Spitch")
client = Spitch()

# Get the path to the audio file and the language code
text = input("Enter the text: ")
lang = input("Enter the language code: ")

# Generate the tone markings
response = client.text.tone_mark(
    language=lang,
    text=text
)

# Print the marked text
print(response.text)  