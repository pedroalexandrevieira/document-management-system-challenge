import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Header from '../components/shared/Header';
import Footer from '../components/shared/Footer';
import DocumentDetail from '../components/documents/DocumentDetail';

const DocumentPage = () => {
  const { id } = useParams();
  const [document, setDocument] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/documents/${id}`)
      .then((response) => setDocument(response.data))
      .catch((error) => console.error('Error fetching document:', error));
  }, [id]);

  return (
    <>
      <Header />
      <div className="container">
        <h1>Document Details</h1>
        <DocumentDetail document={document} />
      </div>
      <Footer />
    </>
  );
};

export default DocumentPage;
