from backend.database import db
from flask import Flask
from dotenv import load_dotenv
from backend.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

def initialize_database():
    """
    Creates all tables defined in the models.
    """
    with app.app_context():
        db.create_all()  # Automatically generates SQL to create tables
        print("Tables created successfully.")

if __name__ == "__main__":
    initialize_database()