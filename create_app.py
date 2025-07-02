from flask import Flask
from config import Config
from extensions import db, login_manager
from routes.main import main_bp
from routes.auth import auth_bp
from routes.fiesta import fiesta_bp
from routes.parcela import parcela_bp
from routes.perfil import perfil_bp
from routes.publicidad import publicidad_bp
from utils.sesion import load_user
import locale

def create_app():
    #Configuración del locale para el idioma español
    try:
        #locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # Para Linux/Mac
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252') # Para Windows 
    except locale.Error as e:
        print(f"No se pudo establecer el locale: {e}")
    
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.user_loader(load_user)
    login_manager.login_message = "Inicia sesión para continuar."
        
    #División de rutas en blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(fiesta_bp)
    app.register_blueprint(parcela_bp)
    app.register_blueprint(perfil_bp)
    app.register_blueprint(publicidad_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app
