from flask import Flask
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from controllers.documents import api_blueprint
from database import db

def create_app():
    app = Flask(__name__)  # Initialize Flask app first
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)  # Initialize SQLAlchemy with the app
    CORS(app)  # Enable Cross-Origin Resource Sharing

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Global error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        return {"error": str(e)}, 500

    # Ensure database tables are created
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)