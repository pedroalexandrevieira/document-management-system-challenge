import React from 'react';
import { Card, Container } from 'react-bootstrap';

const DocumentDetail = ({ document }) => {
  if (!document) return <p>Loading...</p>;

  return (
    <Container>
      <Card>
        <Card.Header>{document.process_number}</Card.Header>
        <Card.Body>
          <Card.Title>{document.title || 'Untitled Document'}</Card.Title>
          <Card.Text>
            <strong>Tribunal:</strong> {document.court || 'N/A'}
          </Card.Text>
          <Card.Text>
            <strong>Summary:</strong> {document.summary || 'No Summary Provided'}
          </Card.Text>
          <Card.Text>
            <strong>Content:</strong> {document.content || 'No Content'}
          </Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default DocumentDetail;
