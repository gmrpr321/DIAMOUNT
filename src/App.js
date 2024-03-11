import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Index from "./components/Index";
const App = () => {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="index" element={<Index />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
