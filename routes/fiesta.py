from datetime import datetime
from extensions import db
from models import Fiesta, Ayuntamiento, Parcela, Solicitud, Fiesta_parcela
from forms import FiestaForm
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash, jsonify
from flask_login import login_required, current_user
from utils.db_operaciones import guardar_fiesta, get_solicitudes_fiesta, get_parcelas_solicitadas
from utils.permisos import verificar_permisos, verificar_permisos_fiesta
from utils.helpers import serializa_parcela

fiesta_bp = Blueprint('fiesta', __name__)

@fiesta_bp.route("/ayuntamiento/fiesta", methods=['GET', 'POST'])
@fiesta_bp.route("/ayuntamiento/fiesta/<int:fiesta_id>", methods=['GET', 'POST'])
@login_required
def fiesta_form(fiesta_id=None):
    """Formulario para crear o editar una fiesta"""
    fiesta = Fiesta.query.get(fiesta_id) if fiesta_id else None

    if not verificar_permisos(fiesta):
        abort(403)

    form = FiestaForm(obj=fiesta)

    if form.validate_on_submit():
        fiesta = guardar_fiesta(form, fiesta)
        return redirect(url_for("fiesta.fiesta_view", fiesta_id=fiesta.id))

    return render_template("fiesta/fiesta_form.html", form=form, fiesta=fiesta)


@fiesta_bp.route('/fiesta/<int:fiesta_id>')
def fiesta_view(fiesta_id):
    """Visualización de fiesta"""
    fiesta = Fiesta.get_by_id(fiesta_id)
    if not fiesta:
        abort(403)
    
    ayun = Ayuntamiento.get_by_id(fiesta.idAyun)
    solicitudes = get_solicitudes_fiesta(fiesta_id)
    parcelas_solicitadas = get_parcelas_solicitadas(fiesta_id)

    parcelas_ya_en_fiesta = {parcela.id for parcela in fiesta.parcelas}
    todas_parcelas = Parcela.get_by_Ayun(fiesta.idAyun)

    parcelas_no_en_fiesta = [parcela for parcela in todas_parcelas if parcela.id not in parcelas_ya_en_fiesta]
    parcelas_ordenadas = sorted(fiesta.parcelas, key=lambda p: p.tipo)

    return render_template(
        'fiesta/fiesta_view.html',
        fiesta=fiesta,
        parcelas=[serializa_parcela(p, en_fiesta=True) for p in parcelas_ordenadas], # Solo las que ya están en la fiesta
        parcelas_t=[serializa_parcela(p, en_fiesta=False) for p in parcelas_no_en_fiesta], # Solo las que NO están en la fiesta
        solicitudes=solicitudes,
        ayun=ayun,
        parcelas_solicitadas=parcelas_solicitadas
    )


@fiesta_bp.route("/ayuntamiento/fiesta/eliminar/<int:fiesta_id>", methods=['POST'])
@login_required
def fiesta_delete(fiesta_id):
    fiesta = Fiesta.get_by_id(fiesta_id)

    if not verificar_permisos_fiesta(fiesta):
        abort(403)

    try:
        db.session.delete(fiesta)
        db.session.commit()
        flash("Fiesta eliminada correctamente", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error eliminando fiesta: {str(e)}", "danger")

    return redirect(url_for("main.index"))


@fiesta_bp.route('/ayuntamiento/fiesta/<int:fiesta_id>/añadir/<int:parcela_id>', methods=['POST'])
@login_required
def incluir_parcela_en_fiesta(fiesta_id, parcela_id):
    fiesta = Fiesta.get_by_id(fiesta_id)
    parcela = Parcela.get_by_id(parcela_id)

    if not fiesta or not parcela:
        return jsonify({"success": False, "error": "Fiesta o Parcela no encontrada."}), 404

    if parcela in fiesta.parcelas:
        return jsonify({"success": False, "error": "La parcela ya está añadida."}), 400

    fiesta.parcelas.append(parcela)
    db.session.commit()
    return jsonify({"success": True})


@fiesta_bp.route("/ayuntamiento/fiesta/quitar/<int:parcela_id>/<int:fiesta_id>", methods=['POST'])
@login_required
def fiesta_parcela_delete(parcela_id, fiesta_id):
    """Quitar una parcela de una fiesta y borra las solicitudes asociadas"""
    fiesta = Fiesta.get_by_id(fiesta_id)

    if not verificar_permisos_fiesta(fiesta):
        return jsonify({"success": False, "error": "No autorizado"}), 403

    try:
        db.session.query(Solicitud).filter_by(idParcela=parcela_id, idFiesta=fiesta_id).delete()

        db.session.query(Fiesta_parcela).filter(
            Fiesta_parcela.c.fiesta_id == fiesta_id,
            Fiesta_parcela.c.parcela_id == parcela_id
        ).delete()

        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


@fiesta_bp.route("/ayuntamiento/fiesta/parcela/<int:solicitud_id>/<estado>", methods=['POST'])
@login_required
def solicitud_estado(solicitud_id, estado):
    """Cambia el estado de una solicitud"""
    if not current_user.rol == "ayuntamiento":
        abort(403)

    solicitud = Solicitud.get_by_id(solicitud_id)
    if not solicitud:
        abort(404)

    solicitud.estado = estado
    solicitud.fecha = datetime.utcnow()
    
    db.session.commit()

    flash(f"Estado de la solicitud actualizado a '{estado}'", "success")
    return redirect(url_for("fiesta.fiesta_view", fiesta_id=solicitud.idFiesta))
