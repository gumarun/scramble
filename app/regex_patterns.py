# [全ての半角英数字、アンダースコア] のいずれかを1文字以上要求
user_id_pattern = r'^[A-Za-z0-9_]+$'

# [空白文字以外の文字] を1文字以上要求
username_pattern = r'^\S+$'

# [小文字のアルファベット、全ての数字] を含む文字列を要求
password_pattern = r'^(?=.*[a-z])(?=.*\d)[a-zA-Z0-9-_]+$'