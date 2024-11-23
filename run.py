from app import create_app
from app import db


# アプリケーションを作成
app = create_app()

# アプリケーションを実行
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

# python -B run.py -m dev
