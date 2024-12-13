import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Container, Card } from 'react-bootstrap';

const DocumentPage = () => {
  const { id } = useParams();
  const [document, setDocument] = useState(null);

  useEffect(() => {
    const fetchDocument = async () => {
      try {
        const response = await axios.get(`/api/documents/${id}`);
        setDocument(response.data);
      } catch (error) {
        console.error('Error fetching document:', error);
      }
    };

    fetchDocument();
  }, [id]);

  if (!document) {
    return <div>Loading...</div>;
  }

  return (
    <Container className="mt-4">
      <Card>
        <Card.Header>{document.title || 'Untitled Document'}</Card.Header>
        <Card.Body>
          <p><strong>Processo:</strong> {document.process_number || 'N/A'}</p>
          <p><strong>Tribunal:</strong> {document.tribunal || 'N/A'}</p>
          <p><strong>Sumário:</strong> {document.summary || 'N/A'}</p>
          <p><strong>Descritores:</strong> {document.tags || 'N/A'}</p>
          <p><strong>Decisão:</strong> {document.decision || 'N/A'}</p>
          <p><strong>Conteúdo:</strong> {document.content || 'N/A'}</p>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default DocumentPage;
