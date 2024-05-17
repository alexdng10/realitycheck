import sounddevice as sd
import numpy as np
import speech_recognition as sr
import threading
import os
import pyttsx3
from google.cloud import texttospeech
from openai import OpenAI
from Actual import classify_mood  # Assuming this is your mood classification function
import shlex
client = OpenAI()
cient = texttospeech.TextToSpeechClient()


def speak(text):
    """Converts text to speech using Google Cloud Text-to-Speech."""
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    name="en-US-Studio-O"
    )

    # Select the type of audio file you want
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = cient.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    

    # Save the audio to a file
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    # Play the audio using a suitable library, or manually
    os.system("afplay output.mp3")

def send_message(conversation_history, text, mood, confidence):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": text})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a therapist treating a mental health patient. Use an external classifier to help determine the person's state. Here are the results: the person is {mood} with a confidence level of {confidence}. Keep the conversation casual and friendly, applying Adlerian methods."
                }
            ] + conversation_history,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extract the response content and add to history as assistant's response
        response_content = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": response_content})  # Log the assistant's role with its response
       
        return response_content
    except Exception as e:
        print(f"Error during OpenAI API interaction: {e}")
        return None

def record_audio(samplerate=16000, channels=1, from_file=None):
    if from_file:
        # Load audio from file using suitable library, e.g., librosa or PySoundFile
        import soundfile as sf
        audio_data, fs = sf.read(from_file, dtype='int16')
        if fs != samplerate:
            raise ValueError("Sample rate of file does not match expected sample rate.")
        return audio_data
    else:
        print("Recording... (Press 'Enter' to stop or 'h' to terminate conversation)")
        stop_event = threading.Event()
        audio_data = []
        def callback(indata, frames, time, status):
            if stop_event.is_set():
                raise sd.CallbackStop
            audio_data.append(indata.copy())

        with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback, dtype='int16'):
            input()  # Wait for enter press to stop
            stop_event.set()

        return np.concatenate(audio_data)

def speech_to_text(audio_data, samplerate=16000):
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
    conversation_history = []  # Initialize the conversation history
    try:
        while True:  # Continuous loop until 'h' is pressed
            audio_data = record_audio()
            text = speech_to_text(audio_data)
            if text:
                mood, confidence = classify_mood(text)
                print("Mood classification:", mood, "Confidence:", confidence)
                response = send_message(conversation_history, text, mood, confidence)
                if response:
                    print("Assistant's response:", response)
                    speak(response)
                else:
                    print("Failed to obtain a response from the assistant.")
            else:
                print("Failed to convert speech to text.")
    except KeyboardInterrupt:
        print("Conversation terminated by user.")

if __name__ == "__main__":
    print("Script starting...")
    classify_mood_from_speech()
    print("Script completed.")
