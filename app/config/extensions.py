from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os

bcrypt = Bcrypt()
jwt = JWTManager()

def init_extensions(app):
  bcrypt.init_app(app)

  app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
  app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=20)
  jwt.init_app(app)