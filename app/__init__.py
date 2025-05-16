from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.routes import main, github, content
    app.register_blueprint(main.bp)
    app.register_blueprint(github.bp)
    app.register_blueprint(content.bp)

    with app.app_context():
        db.create_all()

    return app 