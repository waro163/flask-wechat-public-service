import os
import consts
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or consts.SECRECT_KEY
    MAIL_SERVER = consts.MAIL_SERVER#os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = consts.MAIL_PORT#int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = consts.MAIL_USE_TLS#os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = consts.MAIL_USERNAME#os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = consts.MAIL_PASSWORD#os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = consts.MAIL_USERNAME#'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = consts.ADMIN#os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN = consts.WechatToken
    AES_KEY = consts.AES_Key

    @classmethod
    def check_portrait_folder(cls):
        if not os.path.isdir(cls.PORTRAIT_FOLDER):
            os.mkdir(cls.PORTRAIT_FOLDER)

    @staticmethod
    def init_app(app):
        # if not os.path.isdir(Config.PORTRAIT_FOLDER):
        #     os.mkdir(Config.PORTRAIT_FOLDER)
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
