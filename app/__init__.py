from flask import Flask
from pathlib import Path

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = '9308aa751b8cae2711c8afa870a167b3f07ac806d9ee31b3b87a61247f49c00a'
    app.config['DATABASE_PATH'] = Path("Database/usuarios.db")

    from .auth import auth_bp
    from .routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app