from flask import Flask
from flask_mail import Mail, Message
from threading import Thread
from flask_apscheduler import APScheduler
from flask_jwt_extended import JWTManager
from extensions import jwt, db,migrate,mail,manager,scheduler,flask_uuid
import datetime
# import flask_jwt_extended 

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,create_refresh_token,
    get_jwt_identity
)
from flask_cors import CORS

# class Config(object):
#     JOBS=[
#         {
#             'id':'morning',
#             'func':'__main__:send_read_email',
#             'trigger':'cron',
#             'hour':8,
#             'minute':0
#         }
#     ]
# def job_1():   # 一個函式，用來做定時任務的任務。
#     print("HI")


from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # app.config.from_object(Config())
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mstdcfjsudxodu:f143612b550b7065999bd06f4f09ef2156f8edb6d980da4e1e7dc01a2551bf77@ec2-52-71-55-81.compute-1.amazonaws.com:5432/d2ofkbduq9pta0'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    app.secret_key = '2006D625EB0B32A0FAE127417E88FAEF'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_SUPPRESS_SEND'] = False  # 发送邮件，为True则不发送
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # 邮箱服务器
    app.config['MAIL_USE_SSL'] = True  # 重要，qq邮箱需要使用SSL
    app.config['MAIL_USE_TLS'] = False  # 不需要使用TLS
    app.config['MAIL_USERNAME'] = 'Test890305@gmail.com'
    app.config['MAIL_PASSWORD'] = 'bobo0305'
    app.config['JWT_SECRET_KEY'] = '2006D625EB0B32A0FAE127417E88FAEF'

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    # init
    flask_uuid.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app,db)
    manager.__init__(app)
    manager.add_command('db', MigrateCommand)
    scheduler.init_app(app)  # 把任務列表放進flask
    scheduler.start() # 啟動任務列表


    register_endpoints(app)

    return app


def register_endpoints(app):
    @app.before_first_request
    def setup_sqlalchemy():
        db.create_all()
    from app.account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix="/account")
    from app.comic import comic as comic_blueprint
    app.register_blueprint(comic_blueprint, url_prefix="/comic")
    @app.route('/' , methods=['GET'])
    def register():
            return "Hello"

if __name__ == "__main__":
    app=create_app()
    app.run()
