import time, random
from extensions import db
from flask import Blueprint, render_template, send_from_directory, request
from models import Publicidad, Fiesta, Ayuntamiento,Publicitado, Solicitud, Parcela
from flask_login import current_user
from datetime import datetime, timedelta

main_bp = Blueprint('main', __name__)

@main_bp.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "logo.jpeg", mimetype="image/jpeg")

@main_bp.route("/")
def index():
    """Página principal"""
    # Obtener las publicidades activas y las dos aleatorias
    publicidades_Ac_T = Publicidad.get_publicidades_activas() 
    if publicidades_Ac_T:
        random.seed(time.time()) 
        random.shuffle(publicidades_Ac_T) 

        publicidades_mostradas = publicidades_Ac_T[:2] 
    else:
        publicidades_mostradas = []
    
    filtro_descripcion = request.args.get("filtro_descripcion", "")
    publicidades_activas_ids = [pub.id for pub in publicidades_Ac_T]

    query = db.session.query(Publicidad)\
        .join(Publicitado, Publicitado.usuario_id == Publicidad.idPublicitado)\
        .filter(Publicidad.id.in_(publicidades_activas_ids))

    if filtro_descripcion:
        query = query.filter(Publicitado.descripcion.contains(filtro_descripcion))

    publicidades = query.all()

    fiestas = Fiesta.get_all()
    if current_user.is_authenticated and current_user.rol == "ayuntamiento":
        fiestas = Fiesta.query.filter_by(idAyun=current_user.id).all()

    provincias_disponibles = sorted(list(set(ayuntamiento.provincia for ayuntamiento in Ayuntamiento.query.all())))
    provincias_seleccionadas = request.args.getlist("provincias")
    if provincias_seleccionadas:
        fiestas = [fiesta for fiesta in fiestas if fiesta.idAyun and Ayuntamiento.get_by_id(fiesta.idAyun).provincia in provincias_seleccionadas]

    eventos_fiestas = [fiesta.to_event() for fiesta in fiestas]
    
    solicitudes_filtradas = []
    
    if current_user.is_authenticated:
        if current_user.rol == 'feriante':
            solicitudes = Solicitud.get_by_Feriante(current_user.id)
            

            hace_un_mes = datetime.now() - timedelta(days=30)

            for solicitud in solicitudes:
                solicitud.parcela = Parcela.get_by_id(solicitud.idParcela)
                
                if solicitud.fecha >= hace_un_mes:
                    solicitudes_filtradas.append(solicitud)

    return render_template(
        "index.html",
        fiestas=fiestas,
        eventos_fiestas=eventos_fiestas,
        publicidades=publicidades,
        publicidades_T=publicidades_mostradas,
        provincias_disponibles=provincias_disponibles,
        provincias_seleccionadas=provincias_seleccionadas,
        solicitudes_ordenadas = sorted(solicitudes_filtradas, key=lambda s: s.fecha, reverse=True) #para mostrar las más recientes primero
    )