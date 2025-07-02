from models import Admin, db, Fiesta, Solicitud, Parcela, Usuario, Ayuntamiento, Feriante, Publicitado
from flask_login import current_user
from config import Config
from werkzeug.utils import secure_filename
from types import SimpleNamespace
import os


def guardar_fiesta(form, fiesta=None):
    """Guarda o actualiza una fiesta en la base de datos"""
    if fiesta:
        # Actualizar fiesta existente
        fiesta.nombre = form.nombre.data
        fiesta.descripcion = form.descripcion.data
        fiesta.fechaInicio = form.fechaInicio.data
        fiesta.fechaFin = form.fechaFin.data
    else:
        # Crear nueva fiesta
        fiesta = Fiesta(
            idAyun=current_user.id,
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            fechaInicio=form.fechaInicio.data,
            fechaFin=form.fechaFin.data
        )
        db.session.add(fiesta)

    db.session.commit()
    return fiesta

def guardar_parcela(form, parcela=None, idAyun=None, fiesta_id=None):
    """Guarda o actualiza una parcela en la base de datos"""
    coordenadas = form.localizacion.data

    if parcela:
        parcela.idAyun = idAyun
        parcela.nombre = form.nombre.data
        parcela.tipo = form.tipo.data
        parcela.localizacion = coordenadas  
        parcela.detalles = form.detalles.data
    else:
        parcela = Parcela(
            idAyun=current_user.ayuntamiento.usuario_id,
            nombre=form.nombre.data,
            tipo=form.tipo.data,
            localizacion=coordenadas,  
            detalles=form.detalles.data
        )
        db.session.add(parcela)

        if fiesta_id:
            fiesta = Fiesta.query.get(fiesta_id)
            if fiesta:
                fiesta.parcelas.append(parcela)

    db.session.commit()
    return parcela


def get_solicitudes_fiesta(fiesta_id):
    solicitudes = Solicitud.get_by_Fiesta(fiesta_id)
    for solicitud in solicitudes:
        solicitud.parcela = Parcela.get_by_id(solicitud.idParcela)
        solicitud.feriante = Feriante.get_by_id(solicitud.idFeriante)
    return solicitudes

def get_parcelas_solicitadas(fiesta_id):
    """Obtiene las parcelas solicitadas por el feriante logeado para una fiesta"""
    if not (current_user.is_authenticated and current_user.rol == 'feriante'):
        return []

    solicitudes = Solicitud.get_by_FerANDFis(current_user.feriante.usuario_id, fiesta_id)
    for solicitud in solicitudes:
        solicitud.parcela = Parcela.get_by_id(solicitud.idParcela)

    return solicitudes

def guardar_imagen_publicidad(form, publicidad):
    filename = publicidad.foto if publicidad else None  # Mantener imagen anterior si existe

    if form.foto.data and Config.allowed_file(form.foto.data.filename):
        filename = secure_filename(form.foto.data.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        form.foto.data.save(filepath)

    return filename

def obtener_datos_perfil(perfil):
    datos = SimpleNamespace(id=perfil.id, email=perfil.email, rol=perfil.rol)

    if perfil.rol == 'ayuntamiento' and perfil.ayuntamiento:
        datos.nombre = perfil.ayuntamiento.municipio
        datos.descripcion = perfil.ayuntamiento.descripcion
        datos.comunidad_autonoma = perfil.ayuntamiento.comunidad_autonoma
        datos.provincia = perfil.ayuntamiento.provincia
        datos.tlf = perfil.ayuntamiento.tlf
        datos.latitud = perfil.ayuntamiento.latitud
        datos.longitud = perfil.ayuntamiento.longitud

    elif perfil.rol == 'feriante' and perfil.feriante:
        datos.nombre = perfil.feriante.nombre
        datos.tipo = perfil.feriante.tipo
        datos.descripcion = perfil.feriante.descripcion
        datos.tlf = perfil.feriante.tlf

    elif perfil.rol == 'publicitado' and perfil.publicitado:
        datos.nombre = perfil.publicitado.nombre
        datos.descripcion = perfil.publicitado.descripcion
        datos.tlf = perfil.publicitado.tlf
    
    elif perfil.rol == 'admin' and perfil.admin:
        datos.nombre = perfil.admin.nombre
        datos.descripcion = perfil.admin.descripcion
        datos.tlf = perfil.admin.tlf

    return datos

def guardar_perfil(form, perfil=None):
    """Guarda o actualiza un perfil de usuario en la base de datos"""
    if not perfil:
        perfil = Usuario(email=form.email.data, rol=form.rol.data)
        perfil.set_password(form.password.data)
        db.session.add(perfil)
        db.session.commit()

    else:
        perfil.email = form.email.data
        if form.password.data:
            perfil.set_password(form.password.data)

    if perfil.rol == 'ayuntamiento':
        guardar_ayuntamiento(form, perfil)
    elif perfil.rol == 'feriante':
        guardar_feriante(form, perfil)
    elif perfil.rol == 'publicitado':
        guardar_publicitado(form, perfil)
    elif perfil.rol == 'admin':
        guardar_admin(form, perfil)

    db.session.commit()
    return perfil

def guardar_ayuntamiento(form, perfil):
    ayuntamiento = perfil.ayuntamiento or Ayuntamiento(usuario_id=perfil.id)
    ayuntamiento.municipio = form.nombre.data
    ayuntamiento.descripcion = form.descripcion.data
    ayuntamiento.comunidad_autonoma = form.comunidad_autonoma.data
    ayuntamiento.provincia = form.provincia.data
    ayuntamiento.tlf = form.tlf.data
    ayuntamiento.latitud = float(form.latitud.data) if form.latitud.data else ayuntamiento.latitud
    ayuntamiento.longitud = float(form.longitud.data) if form.longitud.data else ayuntamiento.longitud
    db.session.add(ayuntamiento)

def guardar_feriante(form, perfil):
    feriante = perfil.feriante or Feriante(usuario_id=perfil.id)
    feriante.nombre = form.nombre.data
    feriante.tipo = form.tipo.data
    feriante.descripcion = form.descripcion.data
    feriante.tlf = form.tlf.data
    db.session.add(feriante)

def guardar_publicitado(form, perfil):
    publicitado = perfil.publicitado or Publicitado(usuario_id=perfil.id)
    publicitado.nombre = form.nombre.data
    publicitado.descripcion = form.descripcion.data
    publicitado.tlf = form.tlf.data
    db.session.add(publicitado)

def guardar_admin(form, perfil):
    admin = perfil.admin or Admin(usuario_id=perfil.id)
    admin.nombre = form.nombre.data
    admin.descripcion = form.descripcion.data
    admin.tlf = form.tlf.data
    db.session.add(admin)