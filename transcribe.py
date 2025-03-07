# Import modules
from spitch import Spitch
import os

# Instantiate a Spitch client
os.environ["SPITCH_API_KEY"] = os.getenv("Spitch")
client = Spitch()

# Get the path to the audio file and the language code
filename = input("Enter the path to the audio file: ")
lang = input("Enter the language code: ")

# Transcribe the audio file
with open(filename, "rb") as f:
    response = client.speech.transcribe(
    language=lang,
    content=f.read()
    )

# Print the transcribed text
print(response.text)