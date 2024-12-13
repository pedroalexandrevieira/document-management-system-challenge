import React from 'react';
import { Card } from 'react-bootstrap';

const CustomCard = ({ title, text, footer }) => {
  return (
    <Card className="mb-3">
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>{text}</Card.Text>
      </Card.Body>
      {footer && <Card.Footer className="text-muted">{footer}</Card.Footer>}
    </Card>
  );
};

export default CustomCard;
