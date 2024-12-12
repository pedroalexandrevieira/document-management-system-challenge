from backend.database import db
from sqlalchemy import Date, TIMESTAMP

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)  # id (serial4)
    process_number = db.Column(db.String(255))  # process_number (varchar(255))
    summary = db.Column(db.Text)  # summary (text)
    content = db.Column(db.Text)  # content (text)
    relator = db.Column(db.String(255))  # relator (varchar(255))
    court = db.Column(db.String(255))  # tribunal (varchar(255))
    decision = db.Column(db.String(255))  # decision (varchar(255))
    date = db.Column(Date)  # date (date)
    created_at = db.Column(TIMESTAMP)  # created_at (timestamp)
    tags = db.Column(db.Text) 

    # Relationship to Entity
    entities = db.relationship('Entity', backref='document', cascade="all, delete")


class Entity(db.Model):
    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)  # id (serial4)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)  # document_id (int4)
    name = db.Column(db.String(255))  # name (varchar(255))
    label = db.Column(db.String(50))  # label (varchar(50))
    url = db.Column(db.Text)  # url (text)
