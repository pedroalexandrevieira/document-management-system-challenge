import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DocumentListPage from './pages/DocumentListPage';
import DocumentPage from './pages/DocumentPage';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Routes>
      <Route path="/" element={<DocumentListPage />} />
      <Route path="/documents/:id" element={<DocumentPage />} />
    </Routes>
  </Router>
);