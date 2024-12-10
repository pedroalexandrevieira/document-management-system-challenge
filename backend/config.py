import os
from dotenv import load_dotenv

# Load environment variables from a .env file (for development)
load_dotenv()

# Database configuration
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'court_rulings')

# Ensure critical environment variables are set
if not DB_USER or not DB_PASSWORD:
    raise ValueError("Missing database credentials. Ensure DB_USER and DB_PASSWORD are set.")

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
