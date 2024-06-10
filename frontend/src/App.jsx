import { useState } from 'react';
import Input from './components/Input';
import FileCard from './components/FileCard';
import './App.css';

function App() {

  return (
    <>
      <h1>💵 MoneyChat 🤖</h1>
      <FileCard />
      <p className="read-the-docs">
        Click on the Upload File to send the file.
      </p>
      <Input />
      <div id="chat-box"></div>
    </>
  )
}

export default App
