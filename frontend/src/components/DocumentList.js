import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const DocumentListPage = () => {
  const [documents, setDocuments] = useState([]);
  const navigate = useNavigate();

  // Fetch all documents
  const fetchDocuments = async () => {
    try {
      const response = await axios.get('/api/documents'); // Adjust API path if necessary
      setDocuments(response.data);
    } catch (error) {
      console.error('Error fetching documents:', error);
    }
  };

  // Delete a document
  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this document?')) {
      try {
        await axios.delete(`/api/documents/${id}`); // Adjust API path if necessary
        setDocuments(documents.filter((doc) => doc.id !== id));
      } catch (error) {
        console.error('Error deleting document:', error);
      }
    }
  };

  // Navigate to the Document Page
  const handleViewDocument = (id) => {
    navigate(`/documents/${id}`);
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return (
    <div>
      <h1>Document List</h1>
      <table>
        <thead>
          <tr>
            <th>Processo</th>
            <th>Tribunal</th>
            <th>Sumário</th>
            <th>Descritores</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {documents.map((doc) => (
            <tr key={doc.id}>
              <td>{doc.process_number || 'N/A'}</td>
              <td>{doc.tribunal || 'N/A'}</td>
              <td>{doc.summary || 'N/A'}</td>
              <td>{doc.tags || 'N/A'}</td>
              <td>
                <button onClick={() => handleViewDocument(doc.id)}>View</button>
                <button onClick={() => handleDelete(doc.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DocumentListPage;