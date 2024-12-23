# Backend - Document Management System (DMS)

This is the backend for the Document Management System (DMS). It provides a RESTful API to manage court rulings, including CRUD operations for documents, metadata extraction, and entity references. The backend is built with Python, Flask, SQLAlchemy, and PostgreSQL.

---

## Features

- **RESTful API**:
  - Read and Delete court rulings.
  - Extract metadata and entities from raw HTML and JSON files.
- **PostgreSQL Database**:
  - Robust and scalable database for data persistence.
- **Error Handling**:
  - Validates data and handles edge cases gracefully.
- **Docker Support**:
  - Simplifies setup and deployment with Docker.

---

## Prerequisites

To run this project, you need the following:

- **Python 3.8+**: Ensure you have Python installed. [Download here](https://www.python.org/downloads/).
- **PostgreSQL Database**: A relational database for data storage. [Get PostgreSQL](https://www.postgresql.org/download/).

---

## Seed Script Functionality

### 1. **HTML and JSON Processing**
The backend processes legal documents in the form of HTML and JSON files:
- Extracts metadata (e.g., `Processo`, `Relator`, `Tribunal`, `Summary`, `Content`, `Decision`, `Date`, `Created_at`, `Tags`, `Title`.) from HTML using `BeautifulSoup`.
- Extracts entities (e.g., names, labels, URLs) from JSON files.
- Matches HTML files with their corresponding JSON files based on filenames.
- Saves processed documents and entities to the database.

### 2. **Batch Processing**
- Supports bulk processing of files placed in designated directories:
  - `html/` directory for HTML files.
  - `json/` directory for JSON files.
- Automatically logs missing or mismatched files.


### 3. **Logging and Debugging**
- Logs all file processing, database operations, and API requests.
- Detects and reports missing fields, incorrect formats, or database constraints.

---

## Seed Script Usage

1. **Add Your Files**:  Place HTML files in the backend/seed/html/ directory. Place JSON files in the backend/seed/json/ directory.

2. **Run the Batch Processor**:
  python backend/seed/seed.py

3. **Monitor Logs**:
  Logs will display progress and any issues with file processing.

---

## Installation

1. **Create a Virtual Environment(optional)**:
   
   - python3 -m venv venv
   - source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install Dependencies**:
  
   - pip install -r requirements.txt
  
3. **Configure Database**:

    1. **Create a .env file in the backend directory with the following configurations**:

      - DB_USER=your_db_user
      - DB_PASSWORD=your_db_password
      - DB_HOST=localhost
      - DB_PORT=5432
      - DB_NAME=court_rulings

    2. **Initialize database running the script**:

      ```bash
      python backend/scripts/initialize_db.py
      ```

5. **Run the Application**:

    In directory document_system_challenge run the follow command:
    
    ```bash
    python backend/app.py
    ```
---

## Docker Setup

1. **Build the Docker Image**:
   ```bash
    docker build -t dms-backend ./backend
   ```
2. **Run the Container**:
    ```bash
      docker run -d -p 5000:5000 --name dms-backend dms-backend
    ```

---

## API Endpoints

### Document Endpoints

| HTTP Method | Endpoint             | Description                 |
|-------------|----------------------|-----------------------------|
| `GET`       | `/documents`         | Fetch all documents         |
| `GET`       | `/documents/<id>`    | Fetch a specific document   |
| `DELETE`    | `/documents/<id>`    | Delete a document           |

---

## Example Output

### Batch Processing

When processing `exemple.html` and `exemple.json`:

  - Processing: exemple.html and exemple.json
  - Seeded document with ID: 1
  

### API Response

  - Example `GET /documents` response:

  ```json
  [
    {
      "id": 1,
      "process_number": "12345",
      "title": "Court Ruling Title",
      "relator": "Relator Name",
      "court": "Supreme Court",
      "decision": "Decision text",
      "date": "2024-01-01",
      "tags": "tag1, tag2",
      "summary": "Brief summary of the decision",
      "content": "Full document content"
    }
  ]
  ```

## Used Technologies

### Backend
- **Python (3.8+)**: Programming language used for building the backend.
- **Flask**: Lightweight web framework for creating RESTful APIs.
- **SQLAlchemy**: ORM (Object-Relational Mapper) for managing database operations.
- **PostgreSQL**: Robust and scalable relational database for data persistence.
- **BeautifulSoup**: Library for parsing HTML and extracting metadata.
- **Dotenv**: Manages environment variables, such as database credentials, through a `.env` file.
- **Docker**: Containerization tool to simplify setup and ensure consistency across environments.

### Supporting Tools
- **pip**: Python's package manager for installing dependencies.
- **Postman**: Optional tool for testing and debugging API endpoints.
- **Gunicorn**: WSGI server for deploying Flask applications in production.
