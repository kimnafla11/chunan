from cgitb import html
from flask import Blueprint, render_template, request

# Blueplrint 객체 생성
# 첫 번째 : blueprint의 이름
# 두 번째 : 모듈의 이름 main.py에서 app = Flask(__name__, template_folder='view')
blue100 = Blueprint('blue1', __name__)

@blue100.route('/test1')
def test1() :
    html = render_template('sub1/test1.html')
    return html

@blue100.route('/test2')
def test2():
    html = render_template('sub1/test2.html')
    return html