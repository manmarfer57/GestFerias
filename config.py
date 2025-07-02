import os

class Config:
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/gestferias"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Directorio de subida de archivos y extensiones permitidas
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "publicidades")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

    @staticmethod
    def allowed_file(filename):
        return filename and '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
