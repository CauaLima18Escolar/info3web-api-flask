from ..config.db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(60), nullable=False)
    matricula = db.Column(db.String(14), nullable=False, unique=True)

    def __init__(self, data):
        from app import bcrypt
        self.nome = data.get("nome")
        self.email = data.get("email")
        self.senha = bcrypt.generate_password_hash(data.get("senha"), 10)
        self.matricula = data.get("matricula")

    def set_password(self, senha):
        from app import bcrypt
        self.senha = bcrypt.generate_password_hash(senha, 10)
    
    def check_password(self, senha):
        from app import bcrypt
        return bcrypt.check_password_hash(self.senha, senha)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "matricula": self.matricula
        }
    
    @staticmethod
    def validateData(data):
        print("Dados recebidos:", data)
        campos = ["nome", "email", "senha", "matricula"]
        for campo in campos:
            if not data.get(campo):
                print(f"Esse campo aqui está faltando -> '{campo}'")
                return False


    

