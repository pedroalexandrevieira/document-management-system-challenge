import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<DocumentListPage />} />
      <Route path="/documents/:id" element={<DocumentPage />} />
    </Routes>
  </Router>
);

export default App;
