from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from flaskqna import routes




bootstrap=Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()




def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)


     # configure UploadSet
    configure_uploads(app,photos)


  
    # ENV = 'dev'

    # if ENV == 'dev':
    #   app.debug = True
    #   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5433/flaskqna'

    # else:
    #   app.debug = False
    #   app.config['SQLALCHEMY_DATABASE_URI'] = ''

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering  auth brueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix ='/authenticate')

   

    return app