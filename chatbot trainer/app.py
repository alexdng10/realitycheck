
from flask_cors import CORS
from openai import OpenAI
from Actual import classify_mood
from google.cloud import texttospeech
from flask import send_from_directory
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
import os

app = Flask(__name__, static_folder='audio_files')
CORS(app)
client = OpenAI()
text_to_speech_client = texttospeech.TextToSpeechClient()
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, 'audio_files')
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)
def text_to_speech(text):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = text_to_speech_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    filename = 'output.mp3'  # Consider unique naming to handle concurrency
    filepath = os.path.join(app.static_folder, filename)
    with open(filepath, 'wb') as out:
        out.write(response.audio_content)
    return filename
@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data['text']
    conversation_history = data.get('history', [])

    mood, confidence = classify_mood(text)
    response_text = send_message(conversation_history, text, mood, confidence)

    conversation_history.append({"role": "user", "content": text})
    conversation_history.append({"role": "assistant", "content": response_text})

    audio_filename = text_to_speech(response_text)
    audio_url = url_for('static', filename=audio_filename, _external=True)

    return jsonify({
        "response_text": response_text,
        "audio_url": audio_url,
        "conversation_history": conversation_history
    })

def send_message(conversation_history, text, mood, confidence):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Adapt your responses according to the user's mood: {mood}, confidence: {confidence}."}
            ] + conversation_history,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during OpenAI API interaction: {e}")
        return "Sorry, I couldn't generate a response."

if __name__ == '__main__':
    app.run(debug=True)
