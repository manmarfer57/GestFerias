from flask import Blueprint

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
fiesta_bp = Blueprint('fiesta', __name__)
parcela_bp = Blueprint('parcela', __name__)
perfil_bp = Blueprint('perfil', __name__)
publicidad_bp = Blueprint('publicidad', __name__)

from . import main, auth, fiesta, parcela, perfil, publicidad
