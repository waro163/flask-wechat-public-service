from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from myconfig import config

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix = '/wx')
    
    return app