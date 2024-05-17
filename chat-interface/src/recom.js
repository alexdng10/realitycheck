
import React, { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import logo from './mind_check-removebg-preview.png';

const depressionSongs = [
    "https://www.youtube.com/embed/Gs069dndIYk",
    "https://www.youtube.com/embed/I_izvAbhExY",
    "https://www.youtube.com/embed/4G6QDNC4jPs",
    "https://www.youtube.com/embed/VuNIsY6JdUw",
    "https://www.youtube.com/embed/fWNaR-rxAic",
    "https://www.youtube.com/embed/8xG7mH8i-WE"
   
    
];

function SpeechComponent() {
    const navigate = useNavigate();
    const [videoUrl, setVideoUrl] = useState('');
    const [videoIndex, setVideoIndex] = useState(0);
    const [listening, setListening] = useState(false);
    const [error, setError] = useState('');
    const recognitionRef = useRef(null);

    useEffect(() => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRecognition) {
            const recognition = new SpeechRecognition();
            recognitionRef.current = recognition;
            recognition.continuous = true;
            recognition.lang = 'en-US';
            recognition.interimResults = false;

            recognition.onstart = () => {
                setListening(true);
                console.log("Speech recognition started");
            };

            recognition.onresult = (event) => {
                const transcript = event.results[event.resultIndex][0].transcript.trim().toLowerCase();
                console.log('You said:', transcript);
                handleTranscript(transcript);
            };

            recognition.onend = () => {
                if (!recognitionRef.current) return;
                console.log("Speech recognition stopped, restarting...");
                recognition.start();
            };

            recognition.onerror = (event) => {
                setError(`Speech recognition error: ${event.error}`);
                console.error("Speech recognition error:", event.error);
            };

            recognition.start();

            return () => {
                recognition.stop();
                recognitionRef.current = null;
            };
        } else {
            setError('Speech recognition is not supported in this browser.');
        }
    }, []);

    const handleTranscript = (transcript) => {
        console.log("Received Transcript:", transcript);  // This will log every transcript received
    
        const normalizedTranscript = transcript.trim().toLowerCase();
        const triggerPhrases = ["watch", "play", "show", "see", "next song"];
        const stopPhrases = ["stop"];
        
        if (triggerPhrases.some(phrase => normalizedTranscript.includes(phrase))) {
            console.log("Trigger phrase matched:", normalizedTranscript);
            playNextSong();
        } else if (stopPhrases.some(phrase => normalizedTranscript.includes(phrase))) {
            console.log("Stop phrase matched:", normalizedTranscript);
            stopVideo();
        }
    };
    

    const [lastPlayedIndex, setLastPlayedIndex] = useState(-1); // Track the last played song

    const playNextSong = () => {
        // Generate a random index based on the length of the depressionSongs array
        const randomIndex = Math.floor(Math.random() * depressionSongs.length);
        setVideoUrl(''); // Clear the video URL to stop it from playing
        setVideoUrl(depressionSongs[randomIndex]); // Set a new video URL using the random index
    };
    const stopVideo = () => {
        if (recognitionRef.current) {
            recognitionRef.current.stop();
        }
        setVideoUrl(''); // Clear the video URL to stop it from playing
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
                <div className="header">Speech Recognition</div>
                <div className="messages">
                    {videoUrl ? (
                        <div className="video-container">
                            <iframe
                                src={videoUrl}
                                frameBorder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowFullScreen
                            ></iframe>
                        </div>
                    ) : <p>Use voice activation to active your own private playlist!</p>}
                </div>
                <div className="input-section">
          <button className="button" onClick={playNextSong} >Next song</button>
        </div>
            </div>
        </div>
    );
}

export default SpeechComponent;