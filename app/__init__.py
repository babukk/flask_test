
import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import app_config


login_manager = LoginManager()

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()

db_engine, db_base, db_metadata, main_db = None, None, None, None

from . import views, models


def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db_metadata = MetaData(bind=db_engine)
    main_db = SQLAlchemy(app, metadata=db_metadata)
    main_db.init_app(app)
    db_base = declarative_base(db_engine)

    migrate = Migrate(app, db, 'migrations', compare_type=True)

    login_manager.init_app(app)
    login_manager.login_message = "Вы должны авторизоваться для получения доступа."
    login_manager.login_view = 'auth.login'

    Bootstrap(app)

    from .admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint

    app.register_blueprint(home_blueprint)

    return app
