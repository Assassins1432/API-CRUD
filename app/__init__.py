from flask import Flask
from app.routes.benefit_routes import benefit_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(benefit_bp)
    return app
