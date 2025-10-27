from flask import blueprints, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from .db import buscar_usuarios, criar_usuario

auth_bp = blueprints.Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        senha = request.form.get('senha', '')
       
        linha = buscar_usuarios(usuario)
        if linha and check_password_hash(linha['senha'], senha):
            session['USUARIO'] = linha['usuario']
            flash("Login realizado com sucesso.", "success")
            return redirect(url_for('main.portal'))
        else:
            flash("Credenciais inválidas. Tente novamente.", "error")
            return render_template('login.html', erro="Credenciais inválidas. Tente novamente.")
    
    return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'USUARIO' in session:
        return redirect(url_for('main.portal'))
    
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        senha = request.form.get('senha', '')

        OK, msg = criar_usuario(usuario, senha)

        if OK:
            flash("Usuário criado com sucesso. Faça login.", "success")
            return redirect(url_for('auth.login'))
        else:
            flash(msg, "error")
            return render_template('cadastro.html', erro=msg, usuario=usuario)
    
    return render_template('cadastro.html')

@auth_bp.route('/logout')
def logout():   
    session.pop('USUARIO', None)
    return redirect(url_for('auth.login'))