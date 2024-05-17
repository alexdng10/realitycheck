import React, { useState, useRef } from 'react';
import axios from 'axios';

function Chat() {
    const [recording, setRecording] = useState(false);
    const [messages, setMessages] = useState([]);
    const recorderRef = useRef(null);

    const handleStartRecording = () => {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                const MediaRecorder = window.MediaRecorder;
                recorderRef.current = new MediaRecorder(stream);
                recorderRef.current.start();
                setRecording(true);
            }).catch(console.error);
    };

    const handleStopRecording = () => {
        recorderRef.current.stop();
        recorderRef.current.ondataavailable = (e) => {
            const blob = e.data;
            sendAudioToServer(blob);
            recorderRef.current.stream.getTracks().forEach(track => track.stop());  // Ensure this line doesn't throw an error
        };
        setRecording(false);
    };

    const sendAudioToServer = (blob) => {
        const formData = new FormData();
        formData.append('audio', blob, 'filename.wav');
    
        axios.post('http://127.0.0.1:5000/audio', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    return (
        <div>
            <h1>Chat Interface</h1>
            {messages.map((msg, index) => (
                <div key={index} style={{ textAlign: msg.from === 'User' ? 'left' : 'right' }}>
                    {msg.text}
                </div>
            ))}
            <button onClick={recording ? handleStopRecording : handleStartRecording}>
                {recording ? 'Stop' : 'Start'} Recording
            </button>
        </div>
    );
}

export default Chat;
