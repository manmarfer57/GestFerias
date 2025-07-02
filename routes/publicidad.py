from extensions import db
from models import Publicitado, Publicidad
from forms import PublicidadForm
from config import Config
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash, jsonify
from flask_login import login_required, current_user
from datetime import timedelta
import os
from utils.db_operaciones import guardar_imagen_publicidad
from utils.permisos import verificar_permisos_publicidad, verificar_permisos_admin

publicidad_bp = Blueprint('publicidad', __name__)

@publicidad_bp.route("/publicidad/añadir", methods=['GET', 'POST'])
@publicidad_bp.route("/publicidad/añadir/<int:publicidad_id>", methods=['GET', 'POST'])
@login_required
def publicidad_form(publicidad_id=None):
    """Formulario para añadir o editar publicidad"""
    publicidad = Publicidad.query.get(publicidad_id) if publicidad_id else None

    if not verificar_permisos_publicidad(publicidad):
        abort(403)

    form = PublicidadForm(obj=publicidad)

    if form.validate_on_submit():
        if not current_user.es_admin():
            filename = guardar_imagen_publicidad(form, publicidad)

        if publicidad:
            if current_user.es_admin():
                publicidad.fecha = form.fecha.data
            else: 
                publicidad.foto = filename
        else:
            publicidad = Publicidad(
                idPublicitado=current_user.id,
                foto=filename,
                codigo=Publicidad.generar_codigo_unico()
            )
            db.session.add(publicidad)

        db.session.commit()
        flash("Publicidad guardada correctamente", "success")
        return redirect(url_for("publicidad.publicidad_view", publicidad_id=publicidad.id))

    return render_template("publicidad/publicidad_form.html", form=form, publicidad=publicidad)


@publicidad_bp.route('/publicidad/<int:publicidad_id>')
def publicidad_view(publicidad_id):
    publicidad = Publicidad.get_by_id(publicidad_id)

    if publicidad is None:
        abort(404)

    publicitado = Publicitado.get_by_id(publicidad.idPublicitado)

    return render_template('publicidad/publicidad_view.html', publicidad=publicidad, publicitado=publicitado)


@publicidad_bp.route("/aprobar_publicidad/<int:publicidad_id>", methods=["POST"])
@login_required
def aprobar_publicidad(publicidad_id):
    """Aprobar una publicidad (solo admin)"""
    if not verificar_permisos_admin():
        abort(403)

    publicidad = Publicidad.get_by_id(publicidad_id)
    if not publicidad:
        abort(404)

    publicidad.fecha = publicidad.fecha + timedelta(days=30)
    db.session.commit()

    flash("Publicidad aprobada y extendida por 30 días", "success")
    return redirect(url_for("publicidad.publicidad_view", publicidad_id=publicidad.id))


@publicidad_bp.route("/publicidad/eliminar/<int:publicidad_id>", methods=['POST'])
@login_required
def publicidad_delete(publicidad_id):
    publicidad = Publicidad.get_by_id(publicidad_id)
    if not publicidad:
        return jsonify({"success": False, "error": "Publicidad no encontrada."}), 404

    if not (current_user.es_admin() or publicidad.idPublicitado == current_user.id):
        return jsonify({"success": False, "error": "No autorizado"}), 403

    try:
        if publicidad.foto:
            ruta_foto = os.path.join(Config.UPLOAD_FOLDER, publicidad.foto)
            if os.path.exists(ruta_foto):
                os.remove(ruta_foto)

        db.session.delete(publicidad)
        db.session.commit()
        flash("Publicidad eliminada correctamente", "success")
        return redirect(url_for("main.index"))

    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": f"Error eliminando publicidad: {str(e)}"}), 500
