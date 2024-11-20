import pyttsx3

# Initialize the engine
engine = pyttsx3.init('sapi5')

# Get the list of voices
voices = engine.getProperty('voices')

# Set the voice to Microsoft Mark
for voice in voices:
    if "Mark" in voice.name:
        engine.setProperty('voice', voice.id)
        break

# Test the voice
engine.say("Hello, this is Microsoft Mark.")
engine.runAndWait()
