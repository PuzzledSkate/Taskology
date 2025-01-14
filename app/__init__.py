from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        from app.routes import api_blueprint
        app.register_blueprint(api_blueprint)
        
        db.create_all()
    
    return app

