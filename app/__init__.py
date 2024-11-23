from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from instance.Config import config
from instance.Config import Development
from instance.Config import Production
from app.views import main


# 拡張機能のインスタンスを生成
db = SQLAlchemy()


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

    # 各機能のブループリントを登録
    app.register_blueprint(main)

    return app

