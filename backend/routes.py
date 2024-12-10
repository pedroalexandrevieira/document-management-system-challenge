from flask import Blueprint
from controllers.documents import get_documents, get_document_by_id, delete_document

api_blueprint = Blueprint('api', __name__)

api_blueprint.route('/documents', methods=['GET'])(get_documents)
api_blueprint.route('/documents/<int:id>', methods=['GET'])(get_document_by_id)
api_blueprint.route('/documents/<int:id>', methods=['DELETE'])(delete_document)