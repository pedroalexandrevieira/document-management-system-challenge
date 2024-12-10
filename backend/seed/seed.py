import json
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database import db
from models import Document, Entity

# Define field mapping for Portuguese to English schema
FIELD_MAPPING = {
    "processo": "process_number",
    "relator": "relator",
    "tribunal": "court",
    "decisão": "decision",
    "data": "date",
    "descritores": "tags",
    "sumário": "summary",
    "conteúdo": "content",
    "título": "title"
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)


def process_html_and_json(html_path, json_path):
    """Processes an HTML and JSON file to extract document data and save it to the database."""
    # Parse the HTML file
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract metadata using FIELD_MAPPING
    extracted_data = {}
    for pt_field, en_field in FIELD_MAPPING.items():
        element = soup.select_one(f'#{pt_field}') or soup.select_one(f'.{pt_field}')
        extracted_data[en_field] = element.get_text(strip=True) if element else None

    # Parse the date field
    date_str = extracted_data.get("date", "")
    if date_str:
        try:
            extracted_data["date"] = datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            print(f"Error parsing date: {date_str}")
            extracted_data["date"] = None

    # Extract main text as fallback
    extracted_data["content"] = (
        soup.select_one('#content').get_text(strip=True)
        if soup.select_one('#content') else soup.get_text(strip=True)
    )

    # Parse the JSON file for entities
    with open(json_path, 'r', encoding='utf-8') as f:
        entities_data = json.load(f).get('entities', [])

    # Save document and entities to the database
    with app.app_context():
        doc = Document(
            process_number=extracted_data.get("process_number"),
            title=extracted_data.get("title"),
            relator=extracted_data.get("relator"),
            court=extracted_data.get("court"),
            decision=extracted_data.get("decision"),
            date=extracted_data.get("date"),
            tags=extracted_data.get("tags"),
            summary=extracted_data.get("summary"),
            content=extracted_data.get("content")
        )
        db.session.add(doc)
        db.session.commit()

        # Save associated entities
        for ent in entities_data:
            entity = Entity(
                document_id=doc.id,
                name=ent['name'],
                label=ent.get('label', ''),
                url=ent['url']
            )
            db.session.add(entity)

        db.session.commit()
        print(f"Seeded document with ID: {doc.id}")


if __name__ == "__main__":
    # Paths to the sample HTML and JSON files
    html_file = './backend/seed/sample_document.html'
    json_file = './backend/seed/sample_document.json'

    with app.app_context():
        db.create_all()
        process_html_and_json(html_file, json_file)
