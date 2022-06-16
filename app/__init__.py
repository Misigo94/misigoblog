from flask import Flask
from config import configurations
from flask_login import login_manager,LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail




bootstrap = Bootstrap()
# Initialise DB
db = SQLAlchemy()
# mail = Mail()
migrate = Migrate(db)
# initialise login manager
login_manager = LoginManager()
# Redirect to the login page
login_manager.login_view = "auth.login"
# Change how secret kkey is generated
login_manager.session_protection = "strong"
photos = UploadSet('photos',IMAGES)
mail = Mail()
def create_app(config_name):

    app =  Flask(__name__)
    app.config.from_object(configurations[config_name])


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)


    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    mail.init_app(app)
    return app
    