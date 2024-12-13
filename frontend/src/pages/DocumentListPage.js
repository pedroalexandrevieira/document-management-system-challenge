import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from '../components/shared/Header';
import Footer from '../components/shared/Footer';
import DocumentList from '../components/documents/DocumentList';

const DocumentListPage = () => {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    axios.get('/api/documents')
      .then((response) => setDocuments(response.data))
      .catch((error) => console.error('Error fetching documents:', error));
  }, []);

  const handleDelete = (id) => {
    axios.delete(`/api/documents/${id}`)
      .then(() => setDocuments((prev) => prev.filter((doc) => doc.id !== id)))
      .catch((error) => console.error('Error deleting document:', error));
  };

  return (
    <>
      <Header />
      <div className="container">
        <h1>Document List</h1>
        <DocumentList documents={documents} handleDelete={handleDelete} />
      </div>
      <Footer />
    </>
  );
};

export default DocumentListPage;
