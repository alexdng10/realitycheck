import sounddevice as sd
import numpy as np
import speech_recognition as sr
from Actual import classify_mood

def record_audio(duration=5, samplerate=16000):
    """
    Record audio for a given duration and samplerate, returning a NumPy array of the audio.
    """
    print("Recording...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print("Recording stopped.")
    return audio.flatten()

def speech_to_text(audio_data, samplerate=16000):
    """
    Convert recorded audio data to text using Google's Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def classify_mood_from_speech():
    """
    Record speech, convert to text, and classify mood.
    """
    audio_data = record_audio()
    text = speech_to_text(audio_data)
    if text:
        mood_prediction = classify_mood(text)
        print("The mood prediction for the text is:", mood_prediction[0], "and the confidence level is", mood_prediction[1])
    else:
        print("Failed to convert speech to text.")

# Main function call to start the mood classification from speech
if __name__ == "__main__":
    classify_mood_from_speech()