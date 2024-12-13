from flask import Blueprint, jsonify
from database import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/documents', methods=['GET'])
def get_documents():
    from models import Document 
    docs = Document.query.with_entities(
        Document.id, Document.process_number, Document.court, Document.summary, Document.title
    ).all()
    result = []
    for d in docs:
        result.append({
            "id": d.id,
            "process_number": d.process_number,
            "court": d.court,
            "summary": d.summary,
            "title": d.title,
        })
    return jsonify(result), 200

@api_blueprint.route('/documents/<int:id>', methods=['GET'])
def get_document_by_id(id):
    from models import Document 
    doc = Document.query.filter_by(id=id).first()
    if not doc:
        return jsonify({"error": "Document not found"}), 404

    entities = [{"id": e.id, "name": e.name, "label": e.label, "url": e.url} for e in doc.entities]

    data = {
        "id": doc.id,
        "process_number": doc.process_number,
        "title": doc.title,
        "relator": doc.relator,
        "court": doc.court,
        "decision": doc.decision,
        "date": doc.date.isoformat() if doc.date else None,
        "summary": doc.summary,
        "content": doc.content,
        "created_at": doc.created_at.isoformat() if doc.created_at else None,
        "entities": entities
    }
    return jsonify(data), 200

@api_blueprint.route('/documents/<int:id>', methods=['DELETE'])
def delete_document(id):
    from models import Document 
    doc = Document.query.filter_by(id=id).first()
    if not doc:
        return jsonify({"error": "Document not found"}), 404
    db.session.delete(doc)
    db.session.commit()
    return jsonify({"message": "Document deleted successfully"}), 200