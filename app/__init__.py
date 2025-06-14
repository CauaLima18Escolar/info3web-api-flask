from flask import Flask 
from flask_bcrypt import Bcrypt
from .config.db import db, create_db  
from .routes import register_routes

bcrypt = Bcrypt()

def createApp() :
    app = Flask(__name__)
    bcrypt.init_app(app)
    register_routes(app)
    create_db(app)

    with app.app_context():
        from . import models
        db.create_all()


    return app 

