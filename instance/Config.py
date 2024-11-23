import argparse
import os
from dotenv import load_dotenv


class Basic:
    # キャッシュファイルを作成しないように設定
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

    # .envから環境変数を読み込むための関数
    load_dotenv()

    # 現在のファイルのディレクトリ名を取得
    db_dir = os.path.dirname(__file__).replace('\\', '/')


class Development(Basic):
    """開発環境の設定クラス"""
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_URI_PREFIX = os.getenv('DB_URI_PREFIX')
    DB_NAME = os.getenv('DEV_DB_NAME')
    SQLALCHEMY_DATABASE_URI = f"{DB_URI_PREFIX}{Basic.db_dir}/{DB_NAME}"


class Production(Basic):
    """本番環境の設定クラス"""
    DEBUG = False
    SECRET_KEY = ''
    DB_URI_PREFIX = os.getenv('DB_URI_PREFIX')
    DB_NAME = os.getenv('PROD_DB_NAME')
    SQLALCHEMY_DATABASE_URI = f"{DB_URI_PREFIX}{Basic.db_dir}/{DB_NAME}"


class Settings:
    """実行時に必要な設定をするクラス"""

    def __init__(self):
        self.load_args_settings()

    def load_args_settings(self):
        """argparseを使用してコマンドライン引数を設定"""
        parser = argparse.ArgumentParser(description='起動時のOption設定')

        # 実行モードを追加
        parser.add_argument(
            '-m', '--mode',
            help='[dev]=開発モード, [prod]=本番モード',
            type=str,
            choices=['dev', 'prod'],
            required=True
        )

        # パースされた引数を取得
        args = parser.parse_args()

        # パースされた引数の値を代入
        self._mode = args.mode


config = Settings()
