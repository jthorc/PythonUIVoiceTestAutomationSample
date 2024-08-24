import speech_recognition as sr

class VoiceToText:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

    def listen_and_convert(self):
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Please speak:")
            audio = self.recognizer.listen(source)
            
            try:
                # Recognize speech using Google Web Speech API
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Sorry, I could not understand the audio."
            except sr.RequestError:
                return "Request error from Google Speech Recognition service."

# Usage
if __name__ == "__main__":
    voice_to_text = VoiceToText()
    result = voice_to_text.listen_and_convert()
    print("You said:", result)