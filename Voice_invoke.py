import pyttsx3
import time

class TextToSpeech:
    def __init__(self, voice=0, rate=150, volume=1.0):
        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

        # Set the voice: 0 for male, 1 for female
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)

        # Set the speech rate (words per minute)
        self.engine.setProperty('rate', rate)

        # Set the volume level (0.0 to 1.0)
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        # Make the engine say the text
        self.engine.say(text)

        # Block while processing all the currently queued commands
        self.engine.runAndWait()

    def set_voice(self, voice=0):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)

# Example usage
if __name__ == "__main__":
    tts = TextToSpeech(voice=1, rate=150, volume=1.0)
    tts.speak("Alexa, tell me a joke")
    
    time.sleep(2)
    # Change voice to male and speak again
    tts.set_voice(voice=0)
    tts.speak("Hey Google, what is the weather")