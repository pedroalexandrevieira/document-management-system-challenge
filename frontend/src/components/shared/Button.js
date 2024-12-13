import React from 'react';
import { Button } from 'react-bootstrap';

const CustomButton = ({ text, variant, size, onClick }) => {
  return (
    <Button variant={variant || 'primary'} size={size || 'md'} onClick={onClick}>
      {text}
    </Button>
  );
};

export default CustomButton;
