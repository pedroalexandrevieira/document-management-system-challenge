# Frontend - Document Management System (DMS)

This is the frontend of the **Document Management System (DMS)**. It provides a user-friendly interface to view court rulings, metadata, and entity references. The frontend is built with **React**, styled with **React Bootstrap**, and communicates with the backend through a RESTful API.

---

## Features

- Fetch and display document details dynamically using Axios.
- Display metadata in a structured table format.
- Highlight references to known entities in the document content and link them to their source URLs.
- Responsive design using **React Bootstrap**.

---

## Prerequisites

To run this project, you need the following:

- **Node.js** (v14+): Ensure you have Node.js installed. [Download here](https://nodejs.org/).
- **npm**: Package manager to install dependencies.
- **Backend API**: Ensure the backend for the DMS is running (by default at `http://localhost:5000/api`).

---

## Environment Variables

Create a `.env` file in the root directory to configure environment-specific settings.

### Example `.env` file:
```
REACT_APP_API_BASE_URL=http://localhost:5000/api
```

---

## Installation and Development Server

### Steps to Run the Frontend:

1. **Install Dependencies**:
   Ensure you install all required dependencies by running:
   ```bash
   npm install
   ```

2. **Start the Development Server: After installing the dependencies, start the development server**:
   ```bash
   npm start
   ```

3. **Access the Application: Open your browser and navigate to**:
   ```
   http://localhost:3000
   ```

---

## Used Technologies

1. **React (18+)**: Library for building dynamic user interfaces.
2. **Axios**: HTTP client for communicating with the backend API.
3. **React Router (6+)**: For navigation and routing between application pages.
4. **React Bootstrap**: Pre-styled UI components for responsive design.
5. **Environment Variables**: Used to manage API URLs and other environment-specific configurations.
6. **JavaScript (ES6+)**: Programming language with modern features like `async/await`.
7. **CSS and Bootstrap**: For styling and responsive layouts.


### Supporting Tools
- **Node.js**: Runtime environment for building and running the application.
- **npm**: Package managers for dependency management.
- **Webpack**: Built into React for bundling the application for optimized deployment.

