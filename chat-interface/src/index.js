import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App';
import Result from './Result';
import Recom from './recom'
import './index.css';
import MoodTracker from './MoodTracker'; // Import the new component

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/results" element={<Result />} />
        <Route path="/recom" element={<Recom/>}/>
        <Route path="/mood-tracker" element={<MoodTracker/>} />
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);