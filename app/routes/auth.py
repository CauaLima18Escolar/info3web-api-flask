from flask import request, Blueprint, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from ..models import Usuario
from ..config.db import db

authBP = Blueprint("auth", __name__, url_prefix="/auth")

@authBP.route("/login", methods=["POST"])
def login():
    matricula = request.get_json().get("matricula")
    senha = request.get_json().get("senha")

    usuarioLogado = db.session.query(Usuario).filter_by(matricula=matricula).first()

    if not usuarioLogado:
        return jsonify({ "error": "Usuário inexistente" }), 404

    if not usuarioLogado.check_password(senha):
        return jsonify({ "error": "Senha incorreta" }), 400

    return jsonify({ 
        "usuario": usuarioLogado.to_dict(), 
        "token": create_access_token(usuarioLogado.matricula) 
    }), 200
    
@authBP.route("/registro", methods=["POST"])
@jwt_required()
def registro():
    data = request.get_json()

    valid = Usuario.validateData(data)
    if valid == False:
        return jsonify({ "error": "Preencha os campos obrigatórios" }), 400
    
    usuarioExistente = db.session.query(Usuario).filter_by(matricula=data.get("matricula")).first()

    if usuarioExistente:
        return jsonify({ "error": "Já existe um usuário registrado com essa matrícula" }), 409

    novoUsuario = Usuario(data)
    db.session.add(novoUsuario)
    db.session.commit()

    return jsonify({ "message": "Usuário cadastrado com sucesso. Aguarde a resposta de um admin (líder de sala)" }), 200
