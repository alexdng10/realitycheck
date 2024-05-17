import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'; // Make sure to import axios
import './App.css';
import logo from './mind_check-removebg-preview.png';

function Result() {
  const navigate = useNavigate();
  const [analysisResult, setAnalysisResult] = useState(''); // State to hold the analysis results

  const handleAnalysis = async () => {
    const conversationHistory = JSON.parse(localStorage.getItem('conversationHistory'));
    try {
      const response = await axios.post('http://127.0.0.1:5000/analyze_conversation', { history: conversationHistory });
      setAnalysisResult(response.data.analysis); // Set the fetched analysis result to state
    } catch (error) {
      console.error('Error fetching analysis:', error);
      setAnalysisResult('Failed to fetch analysis.');
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
        <div className="header">Results</div>
        <div className="messages">
          {analysisResult || "No analysis performed yet. Click 'Analyze Results' to get the summary of the conversation."}
        </div>
        <div className="input-section">
          <button className="button" onClick={handleAnalysis}>Analyze Results</button>
        </div>
      </div>
    </div>
  );
}

export default Result;
