from flask_login import UserMixin

from app import db
from app import bcrypt
from app import login_manager


class User(UserMixin, db.Model):
    """ユーザーの基本情報を管理するモデルクラス"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(30), unique=False, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(15), nullable=True)
    link = db.Column(db.String(100), nullable=True)
    intro = db.Column(db.String(150), nullable=True)
    birthday = db.Column(db.Date, nullable=True)

    def __init__(
            self,
            user_id,
            username,
            password,
            location,
            link,
            intro,
            birthday
        ):
        self.user_id = user_id
        self.username = username
        self.set_password(password)
        self.location = location
        self.link = link
        self.intro = intro
        self.birthday = birthday

    def set_password(self, password):
        """パスワードをハッシュ化する

        Args:
            password (str): 平文のパスワード
        """
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """ハッシュ値を平文パスワードが一致するかを比較する

        Args:
            password (str): 平文のパスワード

        Returns:
            bool: 一致する場合はTrue、そうでない場合はFalse
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        """セッションから取得したユーザーIDを基にDBからユーザー情報を取得する

        Args:
            user_id (str): セッションから取得したユーザーID

        Returns:
            str: DBから取得したユーザーオブジェクト
        """
        return User.query.get(int(user_id))
