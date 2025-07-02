from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField, DateField, FileField, ValidationError
from wtforms.validators import DataRequired, Email, Length, Optional, Regexp
from utils.locations import PROVINCIAS, COMUNIDADES_AUTONOMAS


class SignupForm(FlaskForm):
    
    email = StringField(
        'Correo Electrónico: ', 
        description="Introduce el correo electrónico de la empresa (ej: usuario@dominio.com) que usarás para la plataforma.",
        validators=[
            DataRequired(message="El correo electrónico es obligatorio."),
            Email(message="Ingresa un correo electrónico válido."),
            Length(max=100, message="El correo electrónico no puede superar los 100 caracteres.")
        ]
    )
    
    password = PasswordField(
        'Contraseña: ', 
        description="Debe tener 4 caracteres como mínimo.",
        validators=[
            DataRequired(message="La contraseña es obligatoria."),
            Length(min=4, message="La contraseña debe tener al menos 4 caracteres."),
        ]
    )

    rol = SelectField(
        'Gestionar un Perfil de: ', 
        description="Selecciona el tipo de usuario.",
        choices=[
            ('ayuntamiento', 'Ayuntamiento'),
            ('feriante', 'Feriante'),
            ('publicitado', 'Publicitado'),
            ('admin', 'Admin')
        ],
        validators=[DataRequired(message="Debes seleccionar un rol.")]
    )
    
    def __init__(self, roles=None, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if roles:
            self.rol.choices = roles
            
    submit = SubmitField('Registrar')

    nombre = StringField(
        'Nombre: ', 
        description="Introduce nombre completo (máximo 64 caracteres).",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(max=64, message="El nombre no puede superar los 64 caracteres.")
        ]
    )
    
    comunidad_autonoma = SelectField(
        'Comunidad Autónoma: ',
        description="Selecciona la comunidad autónoma correspondiente.",
        choices=COMUNIDADES_AUTONOMAS,
        validators=[Optional()]
    )

    provincia = SelectField(
        'Provincia: ',
        description="Selecciona la provincia correspondiente.",
        choices=PROVINCIAS,
        validators=[Optional()]
    )
    
    tlf = StringField(
        'Número de Teléfono: ', 
        description="Número de teléfono de contacto de la empresa (con exactamente 9 dígitos ej: 600123456).",
        validators=[
            Optional(),
            Regexp(r'^\d{9}$', message="El teléfono debe contener exactamente 9 dígitos numéricos.")
        ]
    )

    latitud = StringField(
        'Latitud:',
        description="Coordenada geográfica en formato decimal (se asigna automáticamente).",
        validators=[Optional()]
    )

    longitud = StringField(
        'Longitud:',
        description="Coordenada geográfica en formato decimal (se asigna automáticamente).",
        validators=[Optional()]
    )

    tipo = SelectField(
        'Tipo de servicio : ', 
        description="Selecciona el tipo de actividad principal que ofrece la empresa.",
        choices=[
            ('Atracciones', 'Atracciones'),
            ('Comida', 'Comida'),
            ('Artículos', 'Artículos'),
            ('Multiservicios', 'Multiservicios'),
            ('Otros', 'Otros')
        ],
        validators=[Optional()]
    )

    descripcion = TextAreaField(
        'Descripción: ',
        description="Breve descripción con la que mostrarte a los demás (máximo 500 caracteres).",
        validators=[Optional(), Length(max=500, message="La descripción no puede superar los 500 caracteres.")]
    )
    
    def validate(self, extra_validators=None):
        rv = super().validate(extra_validators=extra_validators)
        if not rv:
            return False

        if self.rol.data == 'ayuntamiento':
            if not self.comunidad_autonoma.data:
                self.comunidad_autonoma.errors.append("Debes seleccionar la comunidad autónoma a la que pertenece.")
                return False
            if not self.provincia.data:
                self.provincia.errors.append("Debes seleccionar la provincia a la que pertenece.")
                return False
            if not self.tlf.data:
                self.tlf.errors.append("El teléfono es obligatorio.")
                return False

        if self.rol.data == 'feriante':
            if not self.tipo.data:
                self.tipo.errors.append("Debes seleccionar un tipo.")
                return False
            if not self.tlf.data:
                self.tlf.errors.append("El teléfono es obligatorio.")
                return False

        if self.rol.data == 'publicitado':
            if not self.tlf.data:
                self.tlf.errors.append("El teléfono es obligatorio.")
                return False

        return True
    
class FiestaForm(FlaskForm):
    nombre = StringField(
        'Nombre: ',
        description="Nombre con el que es conocida la fiesta.",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(max=100, message="El nombre no puede superar los 100 caracteres.")
        ]
    )
    descripcion = TextAreaField('Descripción: ', description="Breve descripción de las actividades de la misma (máximo 500 caracteres).", validators=[Optional(), Length(max=500, message="La descripción no puede superar los 500 caracteres.")])
    fechaInicio = DateField('Fecha de Inicio: ', format='%Y-%m-%d', validators=[DataRequired(message="Debes seleccionar una fecha de inicio.")])
    fechaFin = DateField('Fecha de Fin: ', format='%Y-%m-%d', validators=[DataRequired(message="Debes seleccionar una fecha de finalización.")])
    submit = SubmitField('Crear Fiesta')
    
    def validate_fechaFin(self, field):
        if self.fechaInicio.data and field.data and field.data < self.fechaInicio.data:
            raise ValidationError("La fecha de finalización debe ser igual o posterior a la fecha de inicio.")

class LoginForm(FlaskForm):
    email = StringField(
        'Correo Electrónico: ', 
        validators=[
            DataRequired(message="El correo electrónico es obligatorio."),
            Email(message="Ingresa un correo electrónico válido.")
        ]
    )
    password = PasswordField(
            'Contraseña: ', 
            validators=[DataRequired(message="La contraseña es obligatoria.")]
        )   
    
    submit = SubmitField('Login')

class PublicidadForm(FlaskForm):
    foto = FileField(
        'Subir Foto: ', 
        description="Carga la imagen de la publicidad que quieres publicar.",
        validators=[DataRequired(message="Debes subir una imagen.")]
    )
    
    fecha = DateField('Fecha de validez: ', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Añadir Publicidad')
    
class ParcelaForm(FlaskForm):
    nombre = StringField(
        'Nombre o Código: ', 
        description="Introduce un nombre o código con distintivos de la parcela para una posterior administración más eficiente.",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(max=64, message="El nombre no puede superar los 64 caracteres.")
        ]
    )
    tipo = SelectField(
        'Tipo / Sector: ', 
        description="Tipo de parcela en función del sector en el que se ubica.",
        choices=[('Atracciones', 'Atracciones'), ('Comida', 'Comida'), ('Artículos', 'Artículos'), ('Otros', 'Otros')],
        validators=[DataRequired(message="Debes seleccionar un tipo.")]
    )
    localizacion = StringField('Coordenadas: ', validators=[DataRequired()])
    detalles = TextAreaField('Descripción: ', description="Detalles importantes de la parcela (usabilidad, dimensiones, terreno, etc).", validators=[Optional(), Length(max=500, message="La descripción no puede superar los 500 caracteres.")])
    submit = SubmitField('Añadir Parcela')