import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Table, Button } from 'react-bootstrap';

const DocumentListPage = () => {
  const [documents, setDocuments] = useState([]);
  const navigate = useNavigate();

  const fetchDocuments = async () => {
    try {
      const response = await axios.get('/api/documents');
      setDocuments(response.data);
    } catch (error) {
      console.error('Error fetching documents:', error);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this document?')) {
      try {
        await axios.delete(`/api/documents/${id}`);
        setDocuments(documents.filter((doc) => doc.id !== id));
      } catch (error) {
        console.error('Error deleting document:', error);
      }
    }
  };

  const handleViewDocument = (id) => {
    navigate(`/documents/${id}`);
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return (
    <div className="container mt-4">
      <h1>Document List</h1>
      <Table striped bordered hover>
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
                <Button
                  variant="primary"
                  size="sm"
                  className="me-2"
                  onClick={() => handleViewDocument(doc.id)}
                >
                  View
                </Button>
                <Button
                  variant="danger"
                  size="sm"
                  onClick={() => handleDelete(doc.id)}
                >
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default DocumentListPage;