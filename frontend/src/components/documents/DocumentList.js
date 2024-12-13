import React from 'react';
import { Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const DocumentList = ({ documents, handleDelete }) => {
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Process Number</th>
          <th>Tribunal</th>
          <th>Summary</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {documents.map((doc) => (
          <tr key={doc.id}>
            <td>{doc.process_number}</td>
            <td>{doc.tribunal}</td>
            <td>{doc.summary || 'No Summary Available'}</td>
            <td>
              <Link to={`/documents/${doc.id}`} className="btn btn-primary btn-sm me-2">
                View
              </Link>
              <Button variant="danger" size="sm" onClick={() => handleDelete(doc.id)}>
                Delete
              </Button>
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default DocumentList;
