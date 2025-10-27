import sqlite3
from flask import current_app
from werkzeug.security import generate_password_hash

def _connect():
    return sqlite3.connect(current_app.config['DATABASE_PATH'])

def buscar_usuarios(usuario: str):
    with _connect() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute('SELECT Id, usuario, senha FROM usuarios WHERE usuario = ?', (usuario,))
        return cur.fetchone()
    
def criar_usuario(usuario: str, senha: str):
    """Tenta criar um novo usuário no banco de dados. retorna uma tupla (sucesso: bool, mensagem: str)."""
    
    usuario = (usuario or '').strip()
    senha = (senha or '')

    if not usuario or not senha:
        return False, "Usuário e senha não podem ser vazios."
    
    if len(usuario) < 3:
        return False, "O nome de usuário deve ter pelo menos 3 caracteres."
    if not (8 <= len(senha) <= 12):
        return False, "A senha deve ter entre 8 e 12 caracteres."
    
    try:
        senha_hash = generate_password_hash(senha)

        with _connect() as conn:
            conn.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', (usuario, senha_hash))
            return True, "Usuário criado com sucesso."
    except sqlite3.IntegrityError:
        return False, "O nome de usuário já existe."