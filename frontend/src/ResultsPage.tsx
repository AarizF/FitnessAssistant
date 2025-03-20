import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Markdown from 'react-markdown';
import "./Page.css";

function ResultsPage() {
    const navigate = useNavigate();
    const [response, setResponse] = useState("");
    
    useEffect(() => {
        const storedResponse = localStorage.getItem("fitnessResponse");
        if (storedResponse) {
            setResponse(JSON.parse(storedResponse).message);
        } else {
            navigate("/");
        }
    }, [navigate]);

    return (
        <div className="background">
          <header className="App-header">
            <h1>Your Personalized Fitness Plan</h1>
            <Markdown>{response}</Markdown>
            <button className='back-button' onClick={() => navigate('/')}>Back</button>
          </header>
        </div>
      );
}

export default ResultsPage;