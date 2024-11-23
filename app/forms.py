from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Regexp

from app.messages import Messages
from app import regex_patterns


class SignupForm(FlaskForm):
    """新規登録フォーム"""
    user_id = StringField(
        validators=[
            DataRequired(message=Messages.USER_ID_REQUIRED_ERROR),
            Length(min=3, max=30, message=Messages.USER_ID_LENGTH_ERROR),
            Regexp(
                regex=regex_patterns.user_id_pattern,
                message=Messages.USER_ID_REGEXP_ERROR
            )
        ],
        render_kw={
            'class': 'form-input user_id',
            'aria-label': 'ユーザーID',
            'autocomplete': 'off'
        }
    )

    username = StringField(
        validators=[
            DataRequired(message=Messages.USERNAME_REQUIRED_ERROR),
            Length(min=2, max=15, message=Messages.USERNAME_LENGTH_ERROR),
            Regexp(
                regex=regex_patterns.username_pattern,
                message=Messages.USER_NAME_REGEXP_ERROR
            )
        ],
        render_kw={
            'class': 'form-input user_name',
            'aria-label': 'ユーザー名',
            'autocomplete': 'off'
        }
    )

    password = PasswordField(
        validators=[
            DataRequired(message=Messages.PASSWORD_REQUIRED_ERROR),
            Length(min=8, max=24, message=Messages.PASSWORD_LENGTH_ERROR),
            Regexp(
                regex=regex_patterns.password_pattern,
                message=Messages.PASSWORD_REGEXP_ERROR
            )
        ],
        render_kw={
            'class': 'form-input',
            'aria-label': 'パスワード',
            'autocomplete': 'off',
        }
    )

    submit = SubmitField('登録')


class LoginForm(FlaskForm):
    """ログインフォーム"""
    user_id = StringField(
        validators=[
            DataRequired(message=Messages.USER_ID_REQUIRED_ERROR)
        ],
        render_kw={
            'class': 'form-input user_id',
            'aria-label': 'ユーザーID',
            'autocomplete': 'off',
        }
    )

    password = PasswordField(
        validators=[
            DataRequired(message=Messages.PASSWORD_REQUIRED_ERROR)
        ],
        render_kw={
            'class': 'form-input',
            'aria-label': 'パスワード',
            'autocomplete': 'off',
        }
    )

    remember_me = BooleanField(
        default=False,
        render_kw={
            'aria-label': 'ログイン状態を維持する',
            'style': 'cursor: pointer',
        }
    )

    submit = SubmitField('ログイン')
