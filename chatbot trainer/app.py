
from flask_cors import CORS
from openai import OpenAI
from Actual import classify_mood
from google.cloud import texttospeech
from flask import send_from_directory
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
import os
import google.generativeai as genai

app = Flask(__name__, static_folder='audio_files')
CORS(app)
client = OpenAI()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-pro')
text_to_speech_client = texttospeech.TextToSpeechClient()
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, 'audio_files')
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

def analyze_conversation(conversation_history):
    # Convert conversation history to a single text string
    conversation_text = "\n".join([f"{entry['role']}: {entry['content']}" for entry in conversation_history])
    

    # Use the Gemini model to analyze the conversation
    try:
        
        response = model.generate_content(f"analyze this data{conversation_text} to the user to see what recommendation they should do and diagnose their mental health problems and summarize their mental helath problems too each time its a new thing go down a new line so it is easy to read display the information in an organized way and be precise talk in first person and like you know try to be as personalize as possible based on the conversation like give meaningful analyzation ")  # Using the insight mode for analysis
        # Assuming that the response format needs to be parsed according to your application needs
        analysis = response._result.candidates[0].content.parts[0].text
        return analysis
    except Exception as e:
        print(f"Error during Gemini AI interaction: {e}")
        return "Analysis could not be completed."
    

def text_to_speech(text):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        name="en-US-Studio-O"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = text_to_speech_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    filename = 'output.mp3'  # Consider unique naming to handle concurrency
    filepath = os.path.join(app.static_folder, filename)
    with open(filepath, 'wb') as out:
        out.write(response.audio_content)
    return filename

@app.route('/analyze_conversation', methods=['POST'])
def analyze():
    data = request.get_json()
    conversation_history = data.get('history', [])
    print(conversation_history)
    analysis_result = analyze_conversation(conversation_history)
    return jsonify({
        "analysis": analysis_result
    })

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
    print(conversation_history)
    return jsonify({
        "response_text": response_text,
        "audio_url": audio_url,
        "conversation_history": conversation_history
    })

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

if __name__ == '__main__':
    app.run(debug=True)
