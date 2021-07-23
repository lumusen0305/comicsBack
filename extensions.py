from flask_apscheduler import APScheduler
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import FlaskUUID

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
manager = Manager()
scheduler = APScheduler()  # 例項化APScheduler
flask_uuid = FlaskUUID()

# manager.add_command('db', MigrateCommand)
