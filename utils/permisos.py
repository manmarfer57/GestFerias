from flask_login import current_user

def verificar_permisos_fiesta(fiesta):
    return current_user.es_admin() or (current_user.rol == "ayuntamiento" and fiesta.idAyun == current_user.id)

def verificar_permisos_publicidad(publicidad):
    if publicidad:
        return publicidad.idPublicitado == current_user.id or current_user.es_admin()
    return current_user.rol == "publicitado" or current_user.es_admin()

def verificar_permisos_admin():
    return current_user.es_admin()

def verificar_permisos(fiesta):
    return current_user.es_admin() or (current_user.rol == "ayuntamiento" and (not fiesta or fiesta.idAyun == current_user.id))
    