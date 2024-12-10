import React, { useEffect, useState } from 'react';
import api from '../services/api';
import DocumentList from '../components/DocumentList';

const DocumentListPage = () => {
  const [documents, setDocuments] = useState([]);
  
  useEffect(() => {
    api.get('/documents')
      .then(res => setDocuments(res.data))
      .catch((error) => {
        console.error('Error fetching documents:', error);
        alert('Error fetching documents');
      });
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Documents</h1>
      <DocumentList documents={documents} setDocuments={setDocuments} />
    </div>
  );
};

export default DocumentListPage;