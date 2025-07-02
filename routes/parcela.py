from extensions import db
from models import Fiesta, Parcela, Solicitud
from forms import ParcelaForm
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
import json
from utils.db_operaciones import guardar_parcela
from utils.helpers import serializa_parcela

parcela_bp = Blueprint('parcela', __name__)

@parcela_bp.route("/ayuntamiento/parcela/<int:idAyun>", methods=['GET', 'POST'])
@parcela_bp.route("/ayuntamiento/fiesta/parcela/<int:idAyun>/<int:fiesta_id>", methods=['GET', 'POST'])
@parcela_bp.route("/ayuntamiento/parcela/<int:idAyun>/<int:parcela_id>", methods=['GET', 'POST'])
@login_required
def parcela_form(idAyun=None, parcela_id=None, fiesta_id=None):
    """Formulario para crear una parcela"""
    if not current_user.rol == "ayuntamiento":
        abort(403)

    parcela = Parcela.query.get(parcela_id) if parcela_id else None
    form = ParcelaForm(obj=parcela)

    if form.validate_on_submit():
        parcela = guardar_parcela(form, parcela, idAyun, fiesta_id)
        return redirect(url_for("parcela.parcela_view", parcela_id=parcela.id))

    parcelas_serializadas = [serializa_parcela(parcela) for parcela in Parcela.get_by_Ayun(idAyun)]
    
    print(parcelas_serializadas)
    
    return render_template("parcela/parcela_form.html", form=form, parcela=parcela, parcelas=parcelas_serializadas)


@parcela_bp.route('/parcela/<int:parcela_id>', methods=['GET'])
@parcela_bp.route('/parcela/<int:parcela_id>/<int:idFiesta>', methods=['GET', 'POST'])
@login_required
def parcela_view(parcela_id, idFiesta=None):
    """Visualización de parcela"""
    parcela = Parcela.get_by_id(parcela_id)
    if not parcela:
        abort(404)

    fiesta = Fiesta.get_by_id(idFiesta) if idFiesta else None
    coordenadas = json.loads(parcela.localizacion) if parcela.localizacion else None
    solicitud_existente = Solicitud.query.filter_by(idParcela=parcela_id, idFeriante=current_user.id, idFiesta=idFiesta).first() if current_user.rol == "feriante" else None

    # Si un feriante hace una solicitud
    if request.method == 'POST' and idFiesta and not solicitud_existente:
        if current_user.rol == 'feriante':
            nueva_solicitud = Solicitud(idParcela=parcela_id, idFeriante=current_user.id, idFiesta=idFiesta, estado='pendiente')
            db.session.add(nueva_solicitud)
            db.session.commit()
            return redirect(url_for("perfil.perfil", perfil_id=current_user.id))
        
    return render_template(
        "parcela/parcela_view.html",
        parcela=parcela,
        fiesta=fiesta,
        coordenadas=coordenadas,
        solicitada=bool(solicitud_existente),
        solicitud=solicitud_existente,
        fiestas_asociadas=parcela.fiestas
    )


@parcela_bp.route('/parcela/eliminar/<int:parcela_id>', methods=['POST'])
@login_required
def parcela_delete(parcela_id):
    parcela = Parcela.get_by_id(parcela_id)
    if not parcela:
        abort(404)

    solicitudes = Solicitud.query.filter_by(idParcela=parcela_id).all()
    for solicitud in solicitudes:
        db.session.delete(solicitud)

    db.session.delete(parcela)
    db.session.commit()

    flash("Parcela eliminada correctamente", "success")
    return redirect(url_for("main.index"))