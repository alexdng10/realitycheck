import sounddevice as sd
import numpy as np
import speech_recognition as sr
import threading
from Actual import classify_mood

def record_audio(samplerate=16000, channels=1):
    """
    Record audio from the microphone and stop when Enter is pressed.
    """
    print("Recording... (Press Enter to stop)")
    stop_event = threading.Event()

    def callback(indata, frames, time, status):
        if stop_event.is_set():
            raise sd.CallbackStop
        audio_data.append(indata.copy())

    audio_data = []
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback, dtype='int16'):
        input()  # Wait for Enter to be pressed
        stop_event.set()

    print("Recording stopped.")
    return np.concatenate(audio_data)

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
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def classify_mood_from_speech():
    print("Starting mood classification process...")
    audio_data = record_audio()
    print("Audio recording complete. Processing text...")
    text = speech_to_text(audio_data)
    if text:

        mood_prediction = classify_mood(text)
        print("The mood prediction for the text is:", mood_prediction[0], "and the confidence level is", mood_prediction[1])
    else:
        print("Failed to convert speech to text.")

if __name__ == "__main__":
    print("Script starting...")
    classify_mood_from_speech()
    print("Script completed.")
    
    

