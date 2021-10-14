## Accept audio from input device and convert to text
import speech_recognition as sr

# Create a speech recognition object
r = sr.Recognizer()

# Convert audio from microphone to text
def text2Speech(): 
    with sr.Microphone() as source: 
        # Read audio data from default microphone
        print("Speak...")
        audio_data = r.record(source, duration=5)
        print("Processing...")

        # Convert to text
        text = r.recognize_google(audio_data, language='en')
        print(text)

# text2Speech()