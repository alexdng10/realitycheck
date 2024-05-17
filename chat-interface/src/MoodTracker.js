import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; // Default calendar styling
import './App.css'; // Your existing CSS for consistent styling
import logo from './mind_check-removebg-preview.png'; // Assuming you want to use the same logo

function MoodTracker() {
    const navigate = useNavigate();
    const [date, setDate] = useState(new Date());
    const [moods, setMoods] = useState({}); // This object will store the mood for each date

    // Function to handle date change
    const onChange = (newDate) => {
        const dateString = newDate.toISOString().split('T')[0]; // Extract the date part only
        if (moods[dateString]) {
            // If mood is already recorded for this date, just update the date state
            setDate(newDate);
        } else {
            // Ask for mood only if not already recorded
            const mood = prompt('How was your mood?', '');
            if (mood) {
                setMoods(prevMoods => ({
                    ...prevMoods,
                    [dateString]: mood
                }));
            }
            setDate(newDate);
        }
    };

    return (
        <div className="App">
            <img src={logo} alt="Logo" className="logo" />
            <div className="sidebar">
                <button onClick={() => navigate('/')}>Chat bot</button>
                <button onClick={() => navigate('/results')}>Results</button>
                <button onClick={() => navigate('/recom')}>Recommendation</button>
                <button onClick={() => navigate('/mood-tracker')}>Mood Tracker</button>
            </div>
            <div className="chat-container">
                <div className="header">Mood Tracker</div>
                <Calendar
                    onChange={onChange}
                    value={date}
                    className="calendar" // You might want to create specific styles for this
                />
                <div className="mood-display">
                    {moods[date.toISOString().split('T')[0]] ? (
                        <p>Mood on {date.toDateString()}: {moods[date.toISOString().split('T')[0]]}</p>
                    ) : (
                        <p>No mood recorded for {date.toDateString()}</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default MoodTracker;
