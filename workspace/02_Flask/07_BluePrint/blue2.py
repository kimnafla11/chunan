from flask import Blueprint, render_template, request

# Blueprint에서 template_folder를 지정하면
# 지정한 폴더에서 html 파일을 찾는다.
# Blueprint에서 사용하는 모든 html파일이 같은 폴더에 있을 경우
# test()함수에서 경로 설정 없이 파일이름만 쓸 수 있음
blue200 = Blueprint('blue2',__name__, template_folder='view/sub2')

@blue200.route('/test3')
def test3():
    #template_folder를 지정했으므로 파일 이름만 
    html = render_template('test3.html')
    return html

@blue200.route('/test4')
def test4():
    html = render_template('test4.html')
    return html