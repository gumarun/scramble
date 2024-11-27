class AuthError():
    """ユーザー登録認、証時のエラーメッセージ"""
    exists_user_id = 'このユーザーIDはすでに使用されています'
    exists_user_name = 'このユーザー名はすでに使用されています'
    invalid_id_or_name = 'ユーザー名またはパスワードが無効です'


class RequiredError():
    """必須項目の未入力エラーメッセージ"""
    user_id = 'ユーザーIDを入力してください'
    username = 'ユーザー名を入力してください'
    password = 'パスワードを入力してください'


class LengthError():
    """文字数制限のエラーメッセージ"""
    user_id = 'ユーザーIDは3~30文字で入力してください'
    username = 'ユーザー名は2文字以上で入力してください'
    password = 'パスワードは8~24文字で入力してください'
    location = '場所は15文字以下で入力してください'
    link = '場所は255文字以下で入力してください'
    intro = '自己紹介は255文字以下で入力してください'
    birthday = '生年月日は数字8桁で入力してください'

class ValidateError:
    """バリデーションエラーメッセージ"""
    invalid_user_id = '無効な文字が含まれています'
    invalid_password_format = 'パスワードはアルファベットと数字を含む必要があります'
    password_mismatch = 'パスワードが一致しません'
    invalid_birthday_year = '1900年から現在の年までの範囲で入力してください'
    invalid_birthday = '入力された生年月日は無効です'


auth_error = AuthError()
required_error = RequiredError()
length_error = LengthError()
validate_error = ValidateError()
