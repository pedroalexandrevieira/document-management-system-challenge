# Backend - Document Management System (DMS)

This is the backend for the Document Management System (DMS). It provides a RESTful API to manage court rulings, including CRUD operations for documents, metadata extraction, and entity references. The backend is built with Python, Flask, SQLAlchemy, and PostgreSQL.

---

## Features

- **RESTful API**:
  - Create, Read, Update, and Delete court rulings.
  - Extract metadata and entities from raw HTML and JSON files.
- **PostgreSQL Database**:
  - Robust and scalable database for data persistence.
- **Error Handling**:
  - Validates data and handles edge cases gracefully.
- **Docker Support**:
  - Simplifies setup and deployment with Docker.

---

## Script Functionality

### 1. **HTML and JSON Processing**
The backend processes legal documents in the form of HTML and JSON files:
- Extracts metadata (e.g., `Processo`, `Relator`, `Tribunal`, `Data`, etc.) from HTML using `BeautifulSoup`.
- Extracts entities (e.g., names, labels, URLs) from JSON files.
- Matches HTML files with their corresponding JSON files based on filenames.
- Saves processed documents and entities to the database.

### 2. **Batch Processing**
- Supports bulk processing of files placed in designated directories:
  - `html/` directory for HTML files.
  - `json/` directory for JSON files.
- Automatically logs missing or mismatched files.

### 3. **CRUD Operations**
- Provides a RESTful API for managing documents and entities:
  - `GET /documents`: Fetch all documents.
  - `GET /documents/<id>`: Fetch a specific document.
  - `POST /documents`: Add a new document.
  - `PUT /documents/<id>`: Update an existing document.
  - `DELETE /documents/<id>`: Delete a document.

### 4. **Logging and Debugging**
- Logs all file processing, database operations, and API requests.
- Detects and reports missing fields, incorrect formats, or database constraints.

---

## Project Structure

```plaintext
backend/
├── app.py                    # Flask application entry point
├── models.py                 # SQLAlchemy models for Document and Entity
├── database.py               # Database configuration and initialization
├── config.py                 # Application configuration (e.g., database URI)
├── seed/
│   ├── html/                 # Directory for HTML files
│   ├── json/                 # Directory for JSON files
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── README.md                 # Project documentation

---

## Prerequisites

To run this project, you need the following:

- **Python 3.8+**: Ensure you have Python installed. [Download here](https://www.python.org/downloads/).
- **PostgreSQL Database**: A relational database for data storage. [Get PostgreSQL](https://www.postgresql.org/download/).
- **Installed Dependencies**: Install the required Python packages listed in `requirements.txt`:
  - Flask
  - SQLAlchemy
  - BeautifulSoup

---

## Installation

1. **Create a Virtual Environment**:
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install Dependencies**:
  pip install -r requirements.txt
  
3.**Configure the Database**:
  Open config.py and set SQLALCHEMY_DATABASE_URI to point to your PostgreSQL database.

4.**Initialize the Database**:
  flask shell
  >>> from database import db
  >>> db.create_all()
  >>> exit()

5.**Run the Application**:
  flask run

---

## Docker Setup

1. **Build the Docker Image**:
   ```bash
   docker build -t dms-backend .

2. **Run the Container**:
docker run -d -p 5000:5000 --name dms-backend dms-backend

---

## Usage of Batch Processing

1. **Add Your Files**:
  Place HTML files in the ./seed/html/ directory.
  Place JSON files in the ./seed/json/ directory.

2. **Run the Batch Processor**:
  python app.py

3. **Monitor Logs**:
  Logs will display progress and any issues with file processing.

---

## API Endpoints

### Document Endpoints

| HTTP Method | Endpoint             | Description                 |
|-------------|----------------------|-----------------------------|
| `GET`       | `/documents`         | Fetch all documents         |
| `GET`       | `/documents/<id>`    | Fetch a specific document   |
| `POST`      | `/documents`         | Add a new document          |
| `PUT`       | `/documents/<id>`    | Update an existing document |
| `DELETE`    | `/documents/<id>`    | Delete a document           |

### Entity Endpoints

| HTTP Method | Endpoint             | Description                 |
|-------------|----------------------|-----------------------------|
| `GET`       | `/entities`          | Fetch all entities          |
| `GET`       | `/entities/<id>`     | Fetch a specific entity     |
