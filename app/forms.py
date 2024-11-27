from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import Optional

from app import regex_patterns
from app.messages import required_error
from app.messages import length_error
from app.messages import validate_error


class RenderKwConfig:
    """各フィールドのrender_kwの共通設定を管理するクラス。
    指定されたクラス名と追加の属性で共通設定を初期化する。

    Args:
        class_name (str): class属性に指定する値
        aria_label (str, optional): aria-label属性に指定する値
        attrs (dict, optional): 任意の追加の属性をキーワード引数として渡す
        bool (bool, optional): チェックボックスの場合はTrueに指定する
        
    Example:
        render_kw = get_str_render_kw(
            'form-input',
            aria_label='ユーザーID'
        )
    """
    @staticmethod
    def _get_render_kw(aria_label, class_name=None, attrs=None, bool=False):
        """共通のrender_kwのベース設定を作成"""
        if attrs is None:
            attrs = {}

        render_kw = {'aria-label': aria_label}

        # チェックボックスの場合は独自のクラス名をセットする
        if bool:
            render_kw['class'] = class_name
        else:
            render_kw['class'] = 'form-input'
            # 追加のクラス名の指定がある場合
            if class_name:
                render_kw['class'] += f" {class_name}"

        render_kw.update(attrs)
        return render_kw

    @staticmethod
    def get_str_render_kw(aria_label, class_name=None, attrs=None):
        """文字列入力フィールド用のrender_kwを生成"""
        return RenderKwConfig._get_render_kw(aria_label, class_name, attrs)

    @staticmethod
    def get_pw_render_kw(aria_label='パスワード', attrs=None):
        """パスワード入力フィールド用のrender_kwを生成"""
        return RenderKwConfig._get_render_kw(
            aria_label=aria_label,
            attrs=attrs
        )

    @staticmethod
    def get_select_render_kw(aria_label, class_name=None, attrs=None):
        """選択フィールド用のrender_kwを生成"""
        return RenderKwConfig._get_render_kw(
            aria_label=aria_label,
            class_name=class_name,
            attrs=attrs
        )

    @staticmethod
    def get_bool_render_kw(aria_label, class_name=None, attrs=None, bool=False):
        """チェックボックス用のrender_kwを生成"""
        return RenderKwConfig._get_render_kw(
            aria_label=aria_label,
            class_name=class_name,
            attrs=attrs,
            bool=bool
        )


class CommonUserForm(FlaskForm):
    """共通のユーザー情報フォーム"""

    username = StringField(
        validators=[
            DataRequired(message=required_error.username),
            Length(min=2, max=30, message=length_error.username),
            Regexp(regex=regex_patterns.username_pattern)
        ],
        render_kw=RenderKwConfig().get_str_render_kw(
            class_name='user-name',
            aria_label='ユーザー名'
        )
    )


class SignupForm(CommonUserForm):
    """新規登録フォーム"""
    user_id = StringField(
        validators=[
            DataRequired(message=required_error.user_id),
            Length(min=3, max=30, message=length_error.user_id),
            Regexp(
                regex=regex_patterns.user_id_pattern,
                message=validate_error.invalid_user_id
            )
        ],
        render_kw=RenderKwConfig().get_str_render_kw(
            class_name='user-id',
            aria_label='ユーザーID'
        )
    )

    password = PasswordField(
        validators=[
            DataRequired(message=required_error.password),
            Length(min=8, max=50, message=length_error.password),
            Regexp(
                regex=regex_patterns.password_pattern,
                message=validate_error.invalid_password_format
            )
        ],
        render_kw=RenderKwConfig().get_pw_render_kw(aria_label='パスワード')
    )

    submit = SubmitField('登録')


class EditProfileForm(CommonUserForm):
    """プロフィール編集フォーム"""
    location = StringField(
        validators=[
            Length(max=15, message=length_error.location),
        ],
        render_kw=RenderKwConfig().get_select_render_kw(
            class_name='location',
            aria_label='場所'
        )
    )
    
    link = StringField(
        validators=[
            Length(max=100, message=length_error.link),
        ],
        render_kw=RenderKwConfig().get_select_render_kw(
            class_name='link',
            aria_label='ウェブサイト'
        )
    )
    
    intro = TextAreaField(
        validators=[
            Length(max=150, message=length_error.intro),
        ],
        render_kw=RenderKwConfig().get_select_render_kw(
            class_name='intro',
            aria_label='自己紹介'
        )
    )
    
    birthday = StringField(
        validators=[
            Optional(),
            Length(min=8, max=8, message=length_error.birthday)
        ],
        render_kw=RenderKwConfig().get_str_render_kw(
            class_name='birthday',
            aria_label='生年月日'
        )
    )

    submit = SubmitField('保存')

    def validate_birthday(self, field):
        """誕生日（YYYYMMDD）をバリデーション"""
        
        # フォームから受け取った値
        birthday_str = field.data.strip()
        
        if len(birthday_str) != 8:
            raise ValidationError
        
        try:
            birthday_date = datetime.strptime(birthday_str, '%Y%m%d').date()
            field.data = birthday_date
        except ValueError:
            raise ValidationError(validate_error.invalid_birthday)
        
        current_year = datetime.now().year
        
        # 年の範囲チェック
        if birthday_date.year < 1900 or birthday_date.year > current_year:
            raise ValidationError(validate_error.invalid_birthday_year)


class LoginForm(FlaskForm):
    """ログインフォーム"""
    user_id = StringField(
        validators=[
            DataRequired(message=required_error.user_id)
        ],
        render_kw=RenderKwConfig().get_str_render_kw(
            class_name='user-id',
            aria_label='ユーザーID'
        )
    )

    password = PasswordField(
        validators=[
            DataRequired(message=required_error.password)
        ],
        render_kw=RenderKwConfig().get_pw_render_kw(aria_label='パスワード')
    )

    remember_me = BooleanField(
        default=False,
        render_kw=RenderKwConfig().get_bool_render_kw(
            class_name='remember-me',
            aria_label='ログイン状態を維持する',
            attrs={'style': 'cursor: pointer'},
            bool=True
        )
    )

    submit = SubmitField('ログイン')
