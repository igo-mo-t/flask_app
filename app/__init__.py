from flask import Flask
from flask_migrate import Migrate
# from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os, config

# app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

# инициализирует расширения
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


# Фабрика приложения
def create_app(config):        
    # создание экземпляра приложения
    app = Flask(__name__)    
    app.config.from_object(config)    
    db.init_app(app)    
    migrate.init_app(app,  db)    
    login_manager.init_app(app)    
    from .main import main as main_blueprint    
    app.register_blueprint(main_blueprint)    
    #from .admin import main as admin_blueprint    
    #app.register_blueprint(admin_blueprint)
    return app

    # import views
from .main import views
    # from . import forum_views
    # from . import admin_views