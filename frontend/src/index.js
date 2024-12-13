import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const DocumentListPage = lazy(() => import('./pages/DocumentListPage'));
const DocumentPage = lazy(() => import('./pages/DocumentPage'));

const App = () => (
  <Router>
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<DocumentListPage />} />
          <Route path="/documents/:id" element={<DocumentPage />} />
          <Route path="*" element={<div>404 - Page Not Found</div>} />
        </Routes>
      </Suspense>
    </div>
  </Router>
);

export default App;
