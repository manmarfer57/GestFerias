from extensions import db
from models import Usuario, Fiesta, Ayuntamiento, Feriante, Publicitado, Publicidad, Parcela, Solicitud, Fiesta_parcela, Admin
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from datetime import date
from utils.helpers import serializa_parcela

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route("/perfil/<int:perfil_id>", methods=['GET', 'POST'])
@login_required
def perfil(perfil_id):
    """Visualización de perfil"""
    if current_user.is_authenticated:
        usu = Usuario.get_by_id(perfil_id)
        if not usu:
            abort(403)
        
        fiestas = None
        parcelas = None
        publicidades = None
        parcelas_serializadas = None
        usuarios = None
        solicitudes_agrupadas = {}
        fiestas_aceptadas = []
        eventos_fiestas= []

        if usu.rol == 'ayuntamiento':
            fiestas = Fiesta.get_by_Ayun(usu.id)
            parcelas = Parcela.get_by_Ayun(usu.id)
            
            parcelas_serializadas=[serializa_parcela(parcela, en_fiesta=False) for parcela in parcelas]
            
        elif usu.rol == 'feriante':
            solicitudes = Solicitud.get_by_Feriante(usu.id)
            for solicitud in solicitudes:
                solicitud.parcela = Parcela.get_by_id(solicitud.idParcela)
                fiesta = Fiesta.get_by_id(solicitud.idFiesta)

                if fiesta not in solicitudes_agrupadas:
                    solicitudes_agrupadas[fiesta] = []
                
                solicitudes_agrupadas[fiesta].append(solicitud)
                
                if solicitud.estado == "aceptada" or solicitud.estado == "pendiente":
                    fiesta = Fiesta.get_by_id(solicitud.idFiesta)
                    
                    if fiesta and fiesta not in fiestas_aceptadas:
                        fiestas_aceptadas.append(fiesta)
                        eventos_fiestas.append(Fiesta.to_event(fiesta))
            
        elif usu.rol == 'publicitado':
            publicidades = Publicidad.get_by_Publicitado(usu.id)
        
        elif usu.rol == 'admin':
            filtro_nombre_publicitado = request.args.get("filtro_nombre_publicitado", "")
            query1 = db.session.query(Publicidad, Publicitado).join(Publicitado, Publicitado.usuario_id == Publicidad.idPublicitado)
            if filtro_nombre_publicitado:
                query1 = query1.filter(Publicitado.nombre.contains(filtro_nombre_publicitado))
                
                
            filtro_nombre = request.args.get("filtro_nombre", "")
            if filtro_nombre:
                usuarios = Usuario.query.filter(Usuario.email.contains(filtro_nombre)).all()
            else:
                usuarios = Usuario.get_all()

            publicidades = query1.all()
                                
        return render_template("perfil/perfil.html", perfil=usu, fiestas=fiestas, parcelas=parcelas_serializadas, publicidades_T=publicidades, solicitudes_agrupadas=solicitudes_agrupadas, usuarios=usuarios, fiestas_aceptadas=fiestas_aceptadas, eventos_fiestas=eventos_fiestas, today=date.today())

    return "Usuario no autenticado", 401


@perfil_bp.route("/admin/usuario/eliminar/<int:usuario_id>", methods=["POST"])
@login_required
def usuario_delete(usuario_id):
    """Elimina un usuario y sus roles asociados"""
    if not (current_user.es_admin() or usuario_id == current_user.id):
        abort(403)

    try:
        db.session.query(Feriante).filter(Feriante.usuario_id == usuario_id).delete()
        db.session.query(Ayuntamiento).filter(Ayuntamiento.usuario_id == usuario_id).delete()
        db.session.query(Publicitado).filter(Publicitado.usuario_id == usuario_id).delete()
        db.session.query(Admin).filter(Admin.usuario_id == usuario_id).delete()

        usuario = Usuario.get_by_id(usuario_id)
        if usuario:
            db.session.delete(usuario)

        db.session.commit()
        flash("Usuario eliminado correctamente", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error eliminando usuario: {str(e)}", "danger")

    return redirect(url_for("main.index"))


@perfil_bp.route('/solicitud/eliminar/<int:solicitud_id>', methods=['POST'])
@login_required
def solicitud_delete(solicitud_id):
    solicitud = Solicitud.get_by_id(solicitud_id)
    if not solicitud:
        abort(404)

    db.session.delete(solicitud)
    db.session.commit()

    flash("Solicitud eliminada correctamente", "success")
    return redirect(url_for("perfil.perfil", perfil_id=current_user.id))

