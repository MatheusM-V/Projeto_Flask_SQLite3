from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = '9308aa751b8cae2711c8afa870a167b3f07ac806d9ee31b3b87a61247f49c00a'

caminho_banco = Path("Database/usuarios.db")

# Funções - Começo

def buscar_usuarios(usuario):
    with sqlite3.connect(caminho_banco) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute('SELECT Id, usuario, senha FROM usuarios WHERE usuario = ?', (usuario,))
        return cur.fetchone()
    
def criar_usuario(usuario, senha):
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
        with sqlite3.connect(caminho_banco) as conn:
            conn.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', (usuario, senha))
            return True, "Usuário criado com sucesso."
    except sqlite3.IntegrityError:
        return False, "O nome de usuário já existe."

# Funções - Fim

#Rotas - Começo

@app.route('/')
def index():

    if "USUARIO" in session:
        return redirect(url_for('portal'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        senha = request.form.get('senha', '').strip()
       
        linha = buscar_usuarios(usuario)
        if linha and linha['senha'] == senha:
            session['USUARIO'] = linha['usuario']
            return redirect(url_for('portal'))
        else:
            return render_template('login.html', erro="Credenciais inválidas. Tente novamente.")
    
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'USUARIO' in session:
        return redirect(url_for('portal'))
    
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        senha = request.form.get('senha', '')

        OK, msg = criar_usuario(usuario, senha)

        if OK:
            return redirect(url_for('login', msg="Usuário criado com sucesso. Faça login."))
        else:
            return render_template('cadastro.html', erro=msg, usuario=usuario)
    
    return render_template('cadastro.html')

@app.route('/portal')
def portal():
    if "USUARIO" not in session:
        return redirect(url_for('login'))
    return render_template('portal.html', usuario=session['USUARIO'])

@app.route('/logout')
def logout():
    session.pop('USUARIO', None)
    return redirect(url_for('login'))

@app.route('/pagina1')
def pagina1():
    return render_template('portais/pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('portais/pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('portais/pagina3.html')

#Rotas - Fim

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)