from .AuthRoutes import authBP
from .PostRoutes import postBP
from .ComentarioRoutes import comentarioBP
from .EventoRoutes import eventoBP

def register_routes(app):
    app.register_blueprint(authBP)
    app.register_blueprint(postBP)
    app.register_blueprint(comentarioBP)
    app.register_blueprint(eventoBP)