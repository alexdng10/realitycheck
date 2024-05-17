import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './App.css'
import logo from './mind_check-removebg-preview.png';
import Result from './Result'
function App() {
  const [recording, setRecording] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [aiResponse, setAiResponse] = useState('');
  const [aiAudio, setAiAudio] = useState('');
  const [conversationHistory, setConversationHistory] = useState([]);
  const navigate = useNavigate();  // Declare useNavigate hook for navigation

  let timeoutId = null;  // Holds the timeout ID for clearing if needed

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
      clearTimeout(timeoutId);  // Clear any existing timeout when new result comes in
      const speechToText = event.results[0][0].transcript;
      setTranscript(speechToText);
      sendTextToServer(speechToText);
    };

    recognition.onspeechend = () => {
      // Start a timeout when the speech ends
      timeoutId = setTimeout(() => {
        recognition.stop();  // Stop recognition after 2 seconds of no speech
      }, 2000);
    };

    recognition.onend = () => {
      setRecording(false);
      clearTimeout(timeoutId);  // Ensure to clear timeout when recognition officially ends
    };
  
    recognition.start();
  };
  
  const sendTextToServer = async (text) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/process_text', { text, history: conversationHistory });
      const newAudioUrl = response.data.audio_url + `?t=${Date.now()}`; // Append timestamp
      setAiResponse(response.data.response_text);
      setAiAudio(newAudioUrl);
      setConversationHistory(prevHistory => [...prevHistory, { role: 'user', content: text }, { role: 'assistant', content: response.data.response_text }]);
      localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
    } catch (error) {
      console.error('Error processing text:', error);
    }
  };

  return (
    <div className="App">
       <img src={logo} alt="Logo" className="logo" />
       <div className="sidebar">
       <button onClick={() => navigate('/')}>Chat bot</button>
        <button onClick={() => navigate('/results')}>Results</button>
        <button onClick={() => navigate('/recom')}>Recommendation</button> 
        <button onClick={() => navigate('/mood-tracker')}>Mood Tracker</button> {/* New button */}
</div>
      <div className="chat-container">
        <div className="header">Chat bot</div>
        <div className="messages">
          {conversationHistory.map((entry, index) => (
            <div key={index} className={`message ${entry.role}`}>{entry.role === 'user' ? 'User' : 'AI'}: {entry.content}</div>
          ))}
        </div>
        <div className="input-section">
          <button className="button" onClick={startSpeechRecognition}>
            {recording ? 'Stop Recognition' : 'Start Recognition'}
          </button>
        </div>
        {aiAudio && <audio controls src={aiAudio} autoPlay />}
      </div>
    </div>
  );
}

export default App;

