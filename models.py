import random, string
from flask import url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from sqlalchemy.orm import joinedload
from datetime import date, datetime, timedelta
from utils.helpers import genera_random_color


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.String(50), nullable=False) 

    admin = db.relationship('Admin', uselist=False, backref='usuario', lazy='joined') 
    ayuntamiento = db.relationship('Ayuntamiento', uselist=False, backref='usuario', lazy='joined')
    feriante = db.relationship('Feriante', uselist=False, backref='usuario', lazy='joined')
    publicitado = db.relationship('Publicitado', uselist=False, backref='usuario', lazy='joined')
    
    def __repr__(self):
        return f'<Usuario {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def es_admin(self):
        return self.rol == 'admin'

    @staticmethod
    def get_by_id(id):
        return Usuario.query.options(
        joinedload(Usuario.ayuntamiento),
        joinedload(Usuario.feriante),
        joinedload(Usuario.publicitado),
        joinedload(Usuario.admin)
    ).get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def get_all():
        return Usuario.query.all()

class Admin(db.Model):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    tlf = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    
    @staticmethod
    def get_by_id(usuario_id):
        return Admin.query.filter(Admin.usuario_id==usuario_id).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


class Ayuntamiento(db.Model):
    __tablename__ = 'ayuntamiento'
    
    id = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    comunidad_autonoma = db.Column(db.String(256), nullable=False)
    provincia = db.Column(db.String(256), nullable=False)
    tlf = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    latitud = db.Column(db.Float, nullable=True)
    longitud = db.Column(db.Float, nullable=True)

    @staticmethod
    def get_by_id(usuario_id):
        return Ayuntamiento.query.filter(Ayuntamiento.usuario_id==usuario_id).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

class Feriante(db.Model):
    __tablename__ = 'feriante'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    tlf = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)

    @staticmethod
    def get_by_id(usuario_id):
        return Feriante.query.filter(Feriante.usuario_id==usuario_id).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

class Publicitado(db.Model):
    __tablename__ = 'publicitado'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    tlf = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)

    @staticmethod
    def get_by_id(usuario_id):
        return Publicitado.query.filter(Publicitado.usuario_id==usuario_id).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
       
Fiesta_parcela = db.Table(
    'fiesta_parcela',
    db.Column('fiesta_id', db.Integer, db.ForeignKey('fiesta.id', ondelete='CASCADE'), primary_key=True),
    db.Column('parcela_id', db.Integer, db.ForeignKey('parcela.id', ondelete='CASCADE'), primary_key=True)
)
    
class Fiesta(db.Model):
    __tablename__ = 'fiesta'

    id = db.Column(db.Integer, primary_key=True)
    idAyun = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    fechaInicio = db.Column(db.Date, nullable=False)
    fechaFin = db.Column(db.Date, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    parcelas = db.relationship('Parcela', secondary=Fiesta_parcela, back_populates='fiestas', lazy=True, passive_deletes=True)

    def __repr__(self):
        return f'<Fiesta {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Fiesta.query.get(id)
    
    @staticmethod
    def get_by_Ayun(idAyun):
        return Fiesta.query.options(joinedload(Fiesta.parcelas)).filter_by(idAyun=idAyun).all()

    
    @staticmethod
    def get_all():
        return Fiesta.query.all()
    
    def to_event(self):
        ayun_id=self.idAyun
        ayuntamiento = Ayuntamiento.get_by_id(ayun_id)
        color = genera_random_color(self.id)
       
        return {
        "title": f"{self.nombre} - {ayuntamiento.municipio}",
        "start": self.fechaInicio.isoformat(),
        "end": (self.fechaFin + timedelta(days=1)).isoformat(),
        "url": url_for('fiesta.fiesta_view', fiesta_id=self.id),
        "backgroundColor": color,
        "borderColor": color 
    }

class Parcela(db.Model):
    __tablename__ = 'parcela'
    
    id = db.Column(db.Integer, primary_key=True)
    idAyun = db.Column(db.Integer, db.ForeignKey('ayuntamiento.usuario_id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(100))
    localizacion = db.Column(db.JSON, nullable=True)
    detalles = db.Column(db.Text)

    solicitudes = db.relationship('Solicitud', backref='parcela', lazy=True)
    fiestas = db.relationship('Fiesta', secondary=Fiesta_parcela, back_populates='parcelas', lazy=True, passive_deletes=True)

    @staticmethod
    def get_by_id(id):
        return Parcela.query.get(id)
    
    @staticmethod
    def get_by_Ayun(idAyun):
        return Parcela.query.filter(Parcela.idAyun==idAyun).all()
    
    @staticmethod
    def get_all():
        return Parcela.query.all()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    
class Solicitud(db.Model):
    __tablename__ = 'solicitud'
    
    id = db.Column(db.Integer, primary_key=True)
    estado= db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idFeriante = db.Column(db.Integer, db.ForeignKey('feriante.usuario_id', ondelete='CASCADE'), nullable=False)
    idParcela = db.Column(db.Integer, db.ForeignKey('parcela.id', ondelete='CASCADE'), nullable=False)
    idFiesta = db.Column(db.Integer, db.ForeignKey('fiesta.id', ondelete='CASCADE'), nullable=False)

    @staticmethod
    def get_by_id(id):
        return Solicitud.query.get(id)
    
    @staticmethod
    def get_by_Fiesta(idFiesta):
        return Solicitud.query.filter(Solicitud.idFiesta==idFiesta).all()
    
    @staticmethod
    def get_by_Feriante(idFeriante):
        return Solicitud.query.filter(Solicitud.idFeriante==idFeriante).all()
    
    @staticmethod
    def get_by_FerANDFis(idFeriante, idFiesta):
        return Solicitud.query.filter_by(idFiesta=idFiesta, idFeriante=idFeriante).all()
    
    @staticmethod
    def get_all():
        return Solicitud.query.all()
    
class Publicidad(db.Model):
    __tablename__ = 'publicidad'

    id = db.Column(db.Integer, primary_key=True)
    idPublicitado = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    foto = db.Column(db.String(256), nullable=False)
    codigo = db.Column(db.String(10), unique=True, nullable=False, default="")

    def __repr__(self):
        return f'<Publicidad {self.foto}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Publicidad.query.get(id)
    
    @staticmethod
    def get_by_Publicitado(idPublicitado):
        return Publicidad.query.filter(Publicidad.idPublicitado==idPublicitado).all()

    @staticmethod
    def generar_codigo_unico(longitud=10):
        """Genera un código único verificando que no exista en la base de datos."""
        while True:
            codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=longitud))
            if not Publicidad.query.filter_by(codigo=codigo).first():
                return codigo
        
    @staticmethod
    def get_publicidades_activas():
        return Publicidad.query.filter(Publicidad.fecha > date.today()).all()
    
    @staticmethod
    def get_all():
        return Publicidad.query.all()

