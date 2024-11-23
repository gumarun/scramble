from flask import Flask
from flask_compress import Compress
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from instance.Config import config
from instance.Config import Development
from instance.Config import Production


# 拡張機能のインスタンスを生成
db = SQLAlchemy()
compress = Compress()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    # Flaskアプリを作成
    app = Flask(__name__, instance_relative_config=True)

    # config設定を読み込む
    if config._mode == 'prod':
        app.config.from_object(Production)
    elif config._mode == 'dev':
        app.config.from_object(Development)

    # 拡張機能をアプリケーションに紐付け
    db.init_app(app)
    compress.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # 未ログイン時のリダイレクト設定
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'ログインしてください。'

    # ブループリントを登録
    from app.views import main
    app.register_blueprint(main)

    return app
