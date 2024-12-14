# Document Management System (DMS)

This project is a full-stack **Document Management System (DMS)** for managing and analyzing court rulings. It consists of:

- A **JavaScript (React)** frontend for displaying and interacting with court rulings.
- A **Python (Flask)** backend providing RESTful APIs for CRUD operations.
- A **PostgreSQL** database for storing court rulings and metadata.
- **Docker** for containerized deployment and development.

---

## Features

- **User-Friendly Interface**: View and manage court rulings with ease.
- **Powerful Backend API**: Provides endpoints for **Read** and **Delete** operations on court rulings.
- **Containerized Deployment**: Easy to deploy and scale using **Docker**.
- **Database Seeding**: Automates initial data population for testing or development purposes.

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
   - Navigate to the `backend/` directory and follow the steps in the `README.md` file to set up the Flask backend and PostgreSQL database.

2. **Frontend**:
   - Navigate to the `frontend/` directory and follow the steps in the `README.md` file to set up the React frontend.

> **Note**: Ensure the backend is running before testing the frontend to avoid API errors.


## Future Enhancements

1. **Add Unit Tests**:
   - Develop comprehensive unit tests for:
     - Frontend components using testing libraries like Jest or React Testing Library.
     - Backend API endpoints using tools like Pytest to ensure reliability and maintainability.

2. **Advanced Search and Filtering**:
   - Implement powerful search functionality with support for:
     - Filters (e.g., by date, court, tags, or relator).
     - Full-text search for better document discovery.
   - Improve the user experience for managing large datasets.

3. **Pagination**:
   - Add server-side pagination for document lists to:
     - Optimize performance for large datasets.
     - Enhance frontend responsiveness with paginated API responses.

4. **Role-Based Access Control (RBAC)**:
   - Introduce user roles such as:
     - **Admin**: Full access to manage documents and users.
     - **Viewer**: Restricted access to view-only operations.
   - Add fine-grained access permissions to enhance application security.

5. **Export and Download Features**:
   - Enable users to export documents or metadata in various formats:
     - **PDF**: For print-friendly access.
     - **CSV/JSON**: For data portability and analysis.

6. **Improved Entity Highlighting**:
   - Enhance the entity highlighting feature by:
     - Allowing dynamic updates to entity labels and links.
     - Enabling custom configurations for different types of entities.

7. **Localization and Multi-Language Support**:
   - Add localization features to:
     - Translate the user interface into multiple languages.
     - Support international users more effectively.

8. **Enhanced Deployment Options**:
   - Streamline deployment by:
     - Implementing CI/CD pipelines for automated testing and deployment.
     - Supporting cloud platforms like AWS, Azure, or Google Cloud.

---

## Final Notes

This project aims to simplify the management and analysis of court rulings with a scalable, modern tech stack.