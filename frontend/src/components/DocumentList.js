import React from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

const DocumentList = ({ documents, setDocuments }) => {
  const navigate = useNavigate();

  const handleDelete = (id) => {
    api.delete(`/documents/${id}`)
      .then(() => {
        setDocuments(prev => prev.filter(doc => doc.id !== id));
      })
      .catch(() => {
        alert('Error deleting document');
      });
  };

  return (
    <table border="1" cellPadding="5" style={{ borderCollapse: 'collapse', width: '100%' }}>
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
        {documents.map(doc => (
          <tr key={doc.id}>
            <td>{doc.processo}</td>
            <td>{doc.tribunal}</td>
            <td>{doc.sumario}</td>
            <td>{doc.descritores}</td>
            <td>
              <button onClick={() => navigate(`/documents/${doc.id}`)}>View</button>
              <button onClick={() => handleDelete(doc.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DocumentList;