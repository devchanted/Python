import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newMessage = { user: message, bot: '' };
    setChatHistory([...chatHistory, newMessage]);

    try {
      const response = await axios.post('http://localhost:5000/chat', { message });
      const botMessage = response.data.response;
      newMessage.bot = botMessage;
      setChatHistory([...chatHistory, newMessage]);
    } catch (error) {
      console.error("Error communicating with the backend", error);
    }
    setMessage('');
  };

  return (
    <div className="App">
      <h1>AI Chatbot</h1>
      <div className="chat-box">
        {chatHistory.map((chat, index) => (
          <div key={index}>
            <p><strong>You:</strong> {chat.user}</p>
            <p><strong>Bot:</strong> {chat.bot}</p>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={message} 
          onChange={(e) => setMessage(e.target.value)} 
          placeholder="Type your message..." 
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;