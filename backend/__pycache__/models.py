from database import db
from sqlalchemy.dialects.postgresql import JSONB

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    processo = db.Column(db.String(50))
    relator = db.Column(db.String(100))
    tribunal = db.Column(db.String(100))
    decisao = db.Column(db.Text)
    data = db.Column(db.Date)
    descritores = db.Column(db.Text)
    sumario = db.Column(db.Text)
    content = db.Column(db.Text)

    entities = db.relationship('Entity', backref='document', cascade="all,delete")

class Entity(db.Model):
    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))