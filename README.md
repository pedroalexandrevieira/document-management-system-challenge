# Document Management System (DMS)

This project is a full-stack **Document Management System (DMS)** designed to streamline the management and analysis of court rulings. It enables users to view, delete, and manage court documents with ease while leveraging a powerful backend API and a scalable database.

---

## Features

- **User-Friendly Interface**: View and manage court rulings with ease.
- **Powerful Backend API**: Provides endpoints for **Read** and **Delete** operations on court rulings.
- **Containerized Deployment**: Easy to deploy and scale using **Docker**.
- **Database Seeding**: Automates initial data population for testing or development purposes.

---

## Design Choices

1. **Frontend**:
   - Built with **React** to provide a dynamic, component-based user interface.
   - Uses **React Bootstrap** for responsive design and styling.
   - **Axios** is used for efficient API communication with the backend.

2. **Backend**:
   - Built with **Flask**, a lightweight and flexible Python web framework.
   - **SQLAlchemy** ORM simplifies database interactions and schema management.
   - **RESTful API** design provides a clean and scalable way to interact with the database.

3. **Database**:
   - **PostgreSQL** was chosen for its robustness, scalability, and support for advanced SQL features.
   - Relationships between documents and entities are managed through foreign keys and SQLAlchemy relationships.

4. **Containerization**:
   - **Docker** ensures consistency across development and production environments.
   - Both frontend and backend are containerized for ease of deployment.

---

## Caveats and Limitations

1. **Caveats**:
   - The system supports only **Read** and **Delete** operations for court rulings. **Create** and **Update** functionality are not implemented.
   - Backend and frontend must be configured to use the same API base URL to function correctly.

2. **Limitations**:
   - The PostgreSQL database must be running before starting the backend; otherwise, API requests will fail with a database connection error.
   - The application does not handle advanced error scenarios like malformed requests or server timeouts.

---

## Potential Improvements

1. **Add Unit Tests**:
   - For both frontend and backend to improve reliability and maintainability.

2. **Implement Full CRUD Functionality**:
   - Add Create and Update endpoints to the backend for managing court rulings.

3. **Enhanced Search and Filtering**:
   - Add support for full-text search and advanced filtering in the frontend.

4. **Pagination**:
   - Implement server-side pagination to handle large datasets more efficiently.

5. **Role-Based Access Control (RBAC)**:
   - Add user roles with permissions for enhanced security.

6. **CI/CD Pipelines**:
   - Automate deployment and testing processes using tools like GitHub Actions or Jenkins.

---

## Prerequisites

Before setting up the project, ensure the following are installed:

- **Node.js** (v14+): Required for the frontend. [Download Node.js](https://nodejs.org/)
- **Python** (v3.8+): Required for the backend. [Download Python](https://www.python.org/)
- **PostgreSQL**: Required for database storage. [Download PostgreSQL](https://www.postgresql.org/)
- **Docker** (Optional): For containerized deployment. [Download Docker](https://www.docker.com/)

---

## Installation and Setup

To set up the project, follow the detailed instructions provided in the respective README files:

1. **Backend**:
   - Navigate to the [`backend/`](./backend/) directory and follow the steps in the `README.md` file to set up the Flask backend and PostgreSQL database.

2. **Frontend**:
   - Navigate to the [`frontend/`](./frontend/) directory and follow the steps in the `README.md` file to set up the React frontend.

> **Note**: Ensure the backend is running before testing the frontend to avoid API errors.

---

## Run the Docker Image

1. **Build the Docker Image**:
   - Navigate to the root directory of the project and run:
     ```bash
     docker-compose up --build
     ```
    This will:
    - Build and start the PostgreSQL, backend, and frontend services.
    - Automatically link the containers using the Docker network.

2. **Access the Application**:
   - Frontend: `http://localhost:3000`

**Notes**:

- Environment Variables: Ensure the .env file is present in the root directory with the following configurations:
```bash
DB_USER=pedrovieira
DB_PASSWORD=pedrovieira
DB_HOST=db
DB_NAME=court_rulings
```

- Rebuild Containers: If you make changes to the code or environment variables, rebuild the containers:
```bash
docker-compose up --build
```

- To stop all running containers, use:
```bash
docker-compose down
```

---

## Final Notes

This project aims to simplify the management and analysis of court rulings with a scalable, modern tech stack.