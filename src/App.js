import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import './App.css';
import Login from './components/Login';
import Signup from './components/Signup';
import Index from './components/Index';
const App = () => {
  
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="index" element={<Index />} />
          <Route path="signup" element={<Signup/>} />
          <Route path="login" element={<Login/>} />
        </Routes>
      </BrowserRouter>
  </div>
  )
}

export default App