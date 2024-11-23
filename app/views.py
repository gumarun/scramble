from flask import Blueprint
from flask import flash

from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import login_user
from flask_login import logout_user

from app.models import db
from app.models import User
from app.forms import SignupForm
from app.forms import LoginForm


# ブループリントを作成
main = Blueprint('main', __name__)


# トップページ
@main.route('/')
def index():
    signup_form = SignupForm()
    login_form = LoginForm()
    return render_template(
        'index.html',
        signup_form=signup_form,
        login_form=login_form
    )


# 新規登録ページ
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    # バリデーションに失敗した場合
    if not form.validate_on_submit():
        form.user_id.data = ''
        return render_template('register.html', form=form)

    # 入力データを正規化
    user_id = form.user_id.data.strip()
    username = form.username.data.strip()
    password = form.password.data.strip()

    # 重複確認
    errors = False

    if User.query.filter_by(user_id=user_id).first():
        flash('このユーザーIDはすでに使用されています', 'error-text')
        errors = True
        form.user_id.data = ''
    if User.query.filter_by(username=username).first():
        flash('このユーザー名はすでに使用されています', 'error-text')
        errors = True
        form.username.data = ''
    if errors:
        return render_template('register.html', form=form)

    # ユーザーを作成し、DBにコミット
    user = User(
        user_id=user_id,
        username=username,
        password=password
    )
    db.session.add(user)
    db.session.commit()

    # ユーザーをログインさせてトップページにリダイレクト
    login_user(user)
    flash('ようこそ！')
    return redirect(url_for('main.index'))


# ログインページ
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # バリデーションに失敗した場合
    if not form.validate_on_submit():
        form.user_id.data = ''
        return render_template('login.html', form=form)

    # 入力データを正規化
    user_id = form.user_id.data.strip()
    password = form.password.data.strip()
    
    user = User.query.filter_by(user_id=user_id).first()

    # 認証に成功した場合
    if user and user.check_password(password):
        login_user(user, remember=form.remember_me.data)
        flash('おかえりなさい！')
        return redirect(url_for('main.index'))

    # 認証に失敗した場合
    form.user_id.data = ''
    flash('ユーザー名またはパスワードが無効です', 'error-text')
    return render_template('login.html', form=form)


# ログアウト
@main.route('/logout')
def logout():
    logout_user()
    flash('ログアウトしました')
    return redirect(url_for('main.index'))
