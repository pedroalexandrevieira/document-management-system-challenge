# Backend - Document Management System

This is the backend for the Document Management System (DMS). It provides a RESTful API to manage court rulings, including CRUD operations for documents, metadata extraction, and entity references. The backend is built with Python, Flask, SQLAlchemy, and PostgreSQL.

---

## Features

- RESTful API for:
  - Creating, reading, updating, and deleting court rulings.
  - Extracting metadata and entities from raw HTML and JSON files.
- PostgreSQL database for data persistence.
- Robust error handling and validation.
- Easy setup with Docker support.

---

## Requirements

- Python 3.9+
- PostgreSQL
- pip (Python package manager)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/dms-backend.git
   cd dms-backend