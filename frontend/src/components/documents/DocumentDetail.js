import React from 'react';
import { Card, Container, Table } from 'react-bootstrap';

const DocumentDetail = ({ document }) => {
  if (!document) return <p>Loading...</p>;

  const { entities = [] } = document; // Entities to highlight (from JSON file)

  const escapeRegExp = (string) => {
    // Escapes characters with special meaning in RegExp
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  };

  // Function to highlight references in the content
  const highlightEntities = (text, entities) => {
    if (!entities || entities.length === 0) return text;

    // Replace references in the text with clickable links
    let highlightedContent = text;

    entities.forEach((entity) => {
      const escapedEntityName = escapeRegExp(entity.name); // Escape special characters
      const regex = new RegExp(`\\b${escapedEntityName}\\b`, 'g'); // Create the RegExp
      highlightedContent = highlightedContent.replace(
        regex,
        `<a href="${entity.url}" target="_blank" style="color: blue; text-decoration: underline;">${entity.name}</a>`
      );
    });  

    return highlightedContent;
  };

  return (
    <Container>
      {/* Title */}
      <h1>{document.title || 'Untitled Document'}</h1>

      {/* Metadata Table */}
      <Card className="my-4">
        <Card.Body>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Processo</th>
                <th>Relator</th>
                <th>Tribunal</th>
                <th>Decisão</th>
                <th>Data</th>
                <th>Descritores</th>
                <th>Sumário</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{document.process_number || 'N/A'}</td>
                <td>{document.relator || 'N/A'}</td>
                <td>{document.court || 'N/A'}</td>
                <td>{document.decision || 'N/A'}</td>
                <td>{document.date || 'N/A'}</td>
                <td>{document.tags || 'N/A'}</td>
                <td>{document.summary || 'No Summary Provided'}</td>
              </tr>
            </tbody>
          </Table>
        </Card.Body>
      </Card>

      {/* Content with Highlighted Entities */}
      <Card>
        <Card.Header>Conteúdo</Card.Header>
        <Card.Body>
          <Card.Text
            dangerouslySetInnerHTML={{
              __html: highlightEntities(document.content || 'No Content Available', entities),
            }}
          />
        </Card.Body>
      </Card>
    </Container>
  );
};

export default DocumentDetail;
