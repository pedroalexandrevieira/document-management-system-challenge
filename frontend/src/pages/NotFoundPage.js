import React from 'react';
import { Container } from 'react-bootstrap';

const NotFoundPage = () => {
  return (
    <Container className="text-center mt-5">
      <h1>404</h1>
      <p>The page you are looking for was not found.</p>
      <a href="/" className="btn btn-primary">
        Go Back Home
      </a>
    </Container>
  );
};

export default NotFoundPage;
