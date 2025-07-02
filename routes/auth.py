from models import Usuario
from forms import SignupForm, LoginForm
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, current_user
from urllib.parse import urlparse
from utils.db_operaciones import obtener_datos_perfil, guardar_perfil

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup/", methods=["GET", "POST"])
@auth_bp.route("/signup/<int:perfil_id>", methods=["GET", "POST"])
def signup_form(perfil_id=None):
    """Formulario de registro o edición de perfil"""
    roles = [
        ('ayuntamiento', 'Ayuntamiento'),
        ('feriante', 'Feriante'),
        ('publicitado', 'Publicitado')
    ]
    if current_user.is_authenticated and current_user.rol == 'admin':
        roles.append(('admin', 'Admin'))

    perfil = Usuario.get_by_id(perfil_id) if perfil_id else None
    if perfil_id and not perfil:
        abort(404)

    us = obtener_datos_perfil(perfil) if perfil else None
    form = SignupForm(roles=roles, obj=us)
    error = None

    if form.validate_on_submit():
        existe_us = Usuario.get_by_email(form.email.data)

        if existe_us and not perfil:
            flash(f'El correo {form.email.data} ya está registrado.', "danger")
            return render_template("signup_form.html", form=form, perfil=perfil, error=error)

        perfil = guardar_perfil(form, perfil)
        
        if not perfil_id: # Si es nuevo, logueamos al usuario
            login_user(perfil)

        flash("Perfil guardado correctamente", "success")
        next_page = request.args.get("next") or url_for("main.index")
        return redirect(next_page)

    return render_template("signup_form.html", form=form, perfil=perfil, error=error)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        us = Usuario.get_by_email(form.email.data)
        if us and us.check_password(form.password.data):
            login_user(us)

            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('main.index')

            flash("Inicio de sesión exitoso", "success")
            return redirect(next_page)

        flash("Correo o contraseña incorrectos", "danger")

    return render_template('login_form.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("Has cerrado sesión correctamente", "info")
    return redirect(url_for('main.index'))