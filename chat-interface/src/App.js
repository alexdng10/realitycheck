import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [recording, setRecording] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [aiResponse, setAiResponse] = useState('');
  const [aiAudio, setAiAudio] = useState('');

  const startSpeechRecognition = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
  
    recognition.onstart = () => {
      setRecording(true);
      setAiAudio(''); // Clear the previous audio URL
      setTranscript('');
      setAiResponse('');
    };
    recognition.onresult = (event) => {
      const speechToText = event.results[0][0].transcript;
      setTranscript(speechToText);
      sendTextToServer(speechToText);
    };
    recognition.onend = () => setRecording(false);
  
    recognition.start();
  };
  
  const sendTextToServer = async (text) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/process_text', { text });
      const newAudioUrl = response.data.audio_url + `?t=${Date.now()}`; // Append timestamp
      setAiResponse(response.data.response_text);
      setAiAudio(newAudioUrl);
    } catch (error) {
      console.error('Error processing text:', error);
    }
  };

  return (
    <div>
      <h1>Chatbot App</h1>
      <button onClick={startSpeechRecognition}>
        {recording ? 'Stop Recognition' : 'Start Recognition'}
      </button>
      <div>
        <h3>User Response:</h3>
        <p>{transcript}</p>
        <h3>AI Response:</h3>
        <p>{aiResponse}</p>
       
        {aiAudio && <audio key={aiAudio} controls src={aiAudio} autoPlay />}
      </div>
    </div>
  );
}

export default App;
