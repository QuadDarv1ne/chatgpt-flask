from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Инициализация объектов
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    # Загружаем переменные окружения из .env
    load_dotenv()

    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Импорт маршрутов
    from .routes import chat, auth
    app.register_blueprint(chat.bp)
    app.register_blueprint(auth.bp)

    return app
