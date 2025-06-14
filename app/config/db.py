from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATA_BASE_URL")
    db.init_app(app)

