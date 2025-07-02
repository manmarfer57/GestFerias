from models import Usuario

def load_user(user_id):
    """Carga el usuario para la sesión de Flask-Login"""
    return Usuario.get_by_id(int(user_id))
