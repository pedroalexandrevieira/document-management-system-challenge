# Document Management System (DMS)

This project is a full-stack **Document Management System (DMS)** for managing and analyzing court rulings. It consists of:

- A **React** frontend for displaying and interacting with court rulings.
- A **Flask** backend providing RESTful APIs for CRUD operations.
- A **PostgreSQL** database for storing court rulings and metadata.
- **Docker** for containerized deployment and development.

---

## Features

- User-friendly interface for managing court rulings.
- Powerful backend API for CRUD operations.
- Containerized deployment for easy scalability.
- Database seeding for initial data population.

---

## Installation and Setup

Follow these steps to set up and run the project locally or using Docker.

### Prerequisites

- **Node.js**: v16+
- **Python**: v3.9+
- **PostgreSQL**: Ensure it’s installed and running.
- **Docker** (optional, for containerized setup)

---

### Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/pedroalexandrevieira/document-management-system-challenge.git
cd document-management-system-challenge


#### 2. Backend Setup

Install Python dependencies:

bash
pip install -r requirements.txt
Create a .env file in the backend directory with the following content:

makefile
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=court_rulings
Initialize the database:

bash
flask db init
flask db migrate
flask db upgrade
Start the backend server:

bash
flask run


#### 3. Frontend Setup

Navigate to the frontend directory:

bash
cd ../frontend
Install Node.js dependencies:

bash
npm install
Create a .env file in the frontend directory with the following content:

arduino
REACT_APP_BACKEND_URL=http://localhost:5000
Start the frontend development server:

bash
npm start


#### 4. Run with Docker (Optional)

Build and start all services (frontend, backend, and database):

bash
docker-compose up --build
Access the application:

Frontend: http://localhost:3000
Backend: http://localhost:5000


#### 5. Database Seeding

Place raw HTML and JSON files in the appropriate directory.

Run the database seeding script:

bash
python backend/seed.py


#### Notes

Make sure to configure your .env files properly before running the app.
For production deployment, consider additional configurations (e.g., HTTPS, scaling, environment variables).

Future Enhancements
Add unit tests for components.
Support advanced search and filtering for documents.
Implement pagination for large document datasets.
