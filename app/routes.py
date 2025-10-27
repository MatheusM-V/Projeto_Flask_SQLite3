from flask import Blueprint, render_template, redirect, url_for, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if 'USUARIO' in session:
        return redirect(url_for('main.portal'))
    return redirect(url_for('auth.login'))

@main_bp.route('/portal')
def portal():
    if "USUARIO" not in session:
        return redirect(url_for('auth.login'))
    return render_template('portal.html', usuario=session['USUARIO'])

@main_bp.route('/pagina1')
def pagina1():
    if "USUARIO" not in session:
        return redirect(url_for('auth.login'))
    return render_template('portais/pagina1.html')

@main_bp.route('/pagina2')
def pagina2():
    if "USUARIO" not in session:
        return redirect(url_for('auth.login'))
    return render_template('portais/pagina2.html')

@main_bp.route('/pagina3')
def pagina3():
    if "USUARIO" not in session:
        return redirect(url_for('auth.login'))
    return render_template('portais/pagina3.html')