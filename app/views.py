from flask import Blueprint
from flask import render_template


# ブループリントを作成
main = Blueprint('main', __name__)


# トップページ
@main.route('/')
def index():
    return render_template('index.html')
