from datetime import date

from flask import Blueprint
from flask import flash
from flask import render_template
from flask import redirect
from flask import url_for

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from app.models import db
from app.models import User
from app.forms import SignupForm
from app.forms import LoginForm
from app.forms import EditProfileForm
from app.messages import auth_error


# ブループリントを作成
main = Blueprint('main', __name__)


def _is_taken(field, value):
    """指定されたフィールドが既に使用されているか確認する

    Args:
        field (str): チェックしたいフィールドの名前
        value (str): チェックする値

    Returns:
        bool: 
            - True: 指定された値がすでに存在する場合
            - False: 指定された値が存在しない場合
    """
    return User.query.filter(getattr(User, field) == value).first() is not None


def _birthday_format(form):
    """生年月日フィールドの形式を整える"""
    if isinstance(form.birthday.data, date):
        form.birthday.data = form.birthday.data.strftime('%Y%m%d')


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

    if not form.validate_on_submit():
        return render_template('register.html', form=form)

    user_id = form.user_id.data.strip()
    username = form.username.data.strip()
    password = form.password.data.strip()

    # 重複確認
    errors = False

    if _is_taken('user_id', user_id):
        flash(auth_error.exists_user_id, 'user-id-error')
        errors = True

    if _is_taken('username', username):
        flash(auth_error.exists_user_name, 'username-error')
        errors = True

    if errors:
        return render_template('register.html', form=form)

    user = User(
        user_id=user_id,
        username=username,
        password=password,
        location=None,
        link=None,
        intro=None,
        birthday=None,
    )
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for('main.index'))


# ログインページ
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    user_id = form.user_id.data.strip()
    password = form.password.data.strip()

    user = User.query.filter_by(user_id=user_id).first()

    # 認証に成功した場合
    if user and user.check_password(password):
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))

    # 認証に失敗した場合
    flash(auth_error.invalid_id_or_name, 'error-text')
    return render_template('login.html', form=form)


# ログアウト
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# プロフィールページ
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


# プロフィール更新
@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    if not form.validate_on_submit():
        _birthday_format(form)
        
        form.username.data = current_user.username
        form.location.data = current_user.location
        form.link.data = current_user.link
        form.intro.data = current_user.intro
        if current_user.birthday:
            form.birthday.data = current_user.birthday.strftime('%Y%m%d')
        else:
            form.birthday.data = form.birthday.data
        
        return render_template('edit_profile.html', form=form)

    new_name = form.username.data.strip()

    if new_name != current_user.username and _is_taken('username', new_name):
        flash(auth_error.exists_user_name, 'error-text username-error')
        return render_template('edit_profile.html', form=form)
    
    current_user.birthday = form.birthday.data
    current_user.username = new_name
    db.session.commit()
    return redirect(url_for('main.profile'))
