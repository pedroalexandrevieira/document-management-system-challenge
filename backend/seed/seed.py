import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask
from backend.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from backend.database import db
from backend.models import Document, Entity
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

def extract_metadata(label, content, soup, regex=False):
    """Extract metadata from content based on a label."""
    if regex:
        match = re.search(rf"{label}\s*(.+)", content, re.IGNORECASE)
        return match.group(1).strip() if match else None
    else:
        element = soup.find(string=lambda text: isinstance(text, str) and label in text)
        if element:
            next_element = element.find_next("font")
            if next_element:
                return next_element.get_text(strip=True)
        return None

def extract_title(soup):
    """Extract title from HTML."""
    title_tag = soup.find("title")
    return title_tag.get_text(strip=True) if title_tag else "Untitled Document"

def extract_summary(soup):
    """Extract summary from the HTML."""
    # Variations of the label
    summary_labels = ["Sumário", "Sumario", "Sum�rio"]
    for label in summary_labels:
        # Find the element containing the label
        element = soup.find(string=lambda text: isinstance(text, str) and label in text)
        if element:
            # Locate the nearest sibling or child elements for content
            parent = element.find_parent("td")
            if parent:
                content = parent.find_next("td")
                if content:
                    return content.get_text(strip=True)
    return "No Summary Found"

def extract_court(soup):
    """Extract court from the HTML."""
    element = soup.find(string=lambda text: isinstance(text, str) and "Tribunal:" in text)
    if element:
        next_element = element.find_next("font")
        return next_element.get_text(strip=True) if next_element else "Supremo Tribunal de Justiça"
    return "Supremo Tribunal de Justiça"

def extract_tags(soup):
    """Extract tags (Descritores) from the HTML."""
    # Variations of the label
    tag_labels = ["Descritores", "Descritor", "Descrit�res"]
    for label in tag_labels:
        # Find the element containing the label
        element = soup.find(string=lambda text: isinstance(text, str) and label in text)
        if element:
            # Locate the nearest sibling or child elements for content
            parent = element.find_parent("td")
            if parent:
                content = parent.find_next("td")
                if content:
                    # Replace <br> tags with commas
                    return content.get_text(strip=True).replace("\n", ", ")
    return "No Tags Found"

def extract_created_at():
    """Return the current timestamp as created_at."""
    return datetime.now()

def clean_main_text(raw_text):
    """
    Clean and normalize main text extracted from the HTML.
    This function removes unnecessary characters, normalizes spaces, and performs additional cleaning.
    """
    # Replace common HTML entities
    cleaned_text = (
        raw_text.replace('&nbsp;', ' ')
        .replace('&#x2019;', "'")
        .replace('&#x201c;', '"')
        .replace('&#x201d;', '"')
        .replace('&amp;', '&')
        .replace('\u00a0', ' ')
        .replace('\u2026', '...')  # Ellipsis
        .replace('\u2013', '-')  # En dash
        .replace('\u2014', '--')  # Em dash
    )

    # Normalize line breaks
    cleaned_text = cleaned_text.replace('\r\n', '\n').replace('\r', '\n')

    # Remove extra spaces, tabs, and normalize multiple line breaks
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)  # Replace multiple newlines with a single newline

    # Remove any unwanted headers, footers, or metadata markers if applicable
    # For example, removing repetitive page headers
    cleaned_text = re.sub(r'^Page \d+\s*', '', cleaned_text, flags=re.MULTILINE)
    cleaned_text = re.sub(r'^\s*-+\s*$', '', cleaned_text, flags=re.MULTILINE)  # Remove horizontal lines

    # Remove common artifacts, such as HTML tags or placeholders left in the text
    cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)  # Remove remaining HTML tags
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)  # Remove text within brackets, e.g., "[See Footnote]"

    # Remove leading and trailing whitespace
    cleaned_text = cleaned_text.strip()

    # Additional processing specific to your dataset
    # For instance, removing custom headers or identifying specific patterns
    cleaned_text = re.sub(r'Document ID: \d+', '', cleaned_text)  # Example: remove document identifiers

    return cleaned_text

def process_html_and_json(html_path, json_path):
    """Processes an HTML and JSON file to extract document data and save it to the database."""
    try:
        with open(html_path, 'r', encoding='ISO-8859-1') as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        html_text = soup.get_text()

        extracted_data = {}
        extracted_data["content"] = clean_main_text(html_text)
        extracted_data["process_number"] = extract_metadata("Processo:", content=html_text, soup=soup, regex=True) or "Unknown Process Number"
        extracted_data["relator"] = extract_metadata("Relator:", content=html_text, soup=soup, regex=True) or "Unknown Relator"
        extracted_data["decision"] = extract_metadata("Decisão:", content=html_text, soup=soup, regex=True) or "No Decision Provided"
        date_str = extract_metadata("Data do Acordão:", content=html_text, soup=soup, regex=True)

        if date_str:
            try:
                extracted_data["date"] = datetime.strptime(date_str, '%d-%m-%Y')
            except ValueError:
                print(f"Error parsing date: {date_str}")
                extracted_data["date"] = None
        else:
            extracted_data["date"] = None

        extracted_data["tags"] = extract_tags(soup)
        extracted_data["summary"] = extract_summary(soup)
        extracted_data["content"] = soup.get_text(strip=True)
        extracted_data["title"] = extract_title(soup)
        extracted_data["court"] = extract_court(soup)
        extracted_data["created_at"] = extract_created_at()

        with open(json_path, 'r', encoding='utf-8') as f:
            json_content = json.load(f)

        if isinstance(json_content, list):
            entities_data = json_content
        elif isinstance(json_content, dict):
            entities_data = json_content.get('entities', [])
        else:
            raise ValueError(f"Unexpected JSON structure in file: {json_path}")

        with app.app_context():
            doc = Document(
                process_number=extracted_data.get("process_number", ""),
                title=extracted_data.get("title", "Untitled Document"),
                relator=extracted_data.get("relator", ""),
                court=extracted_data.get("court", ""),
                decision=extracted_data.get("decision", ""),
                date=extracted_data.get("date"),
                tags=extracted_data.get("tags", ""),
                summary=extracted_data.get("summary", ""),
                content=extracted_data.get("content", ""),
                created_at=extracted_data.get("created_at")
            )
            db.session.add(doc)
            db.session.commit()

            for ent in entities_data:
                entity = Entity(
                    document_id=doc.id,
                    name=ent['name'],
                    label=ent.get('label', ''),
                    url=ent.get('url', '')
                )
                db.session.add(entity)

            db.session.commit()
            print(f"Seeded document with ID: {doc.id}")

    except Exception as e:
        print(f"Error processing {html_path} and {json_path}: {e}")

if __name__ == "__main__":
    html_dir = './backend/seed/html/'
    json_dir = './backend/seed/json/'

    with app.app_context():
        db.create_all()

    for html_file in os.listdir(html_dir):
        if html_file.endswith('.html'):
            html_path = os.path.join(html_dir, html_file)
            json_file = html_file.replace('.html', '.json')
            json_path = os.path.join(json_dir, json_file)

            if os.path.exists(json_path):
                print(f"Processing: {html_file} and {json_file}")
                process_html_and_json(html_path, json_path)
            else:
                print(f"Missing JSON file for: {html_file}")
