# Flask 패키지 설치
# 시작메뉴 > anaconda prompt 실행
# pip install flask

# vscode 하단 파이썬 버전 부분 클릭해서
# base 가 붙어있는 아다콘다 환경으로 변경하고 실행하긔

from flask import Flask, render_template

# 서버 객체 생성
# 첫 번째 : 아무 문자열을 넣어준다.
app = Flask(__name__, template_folder='view')

# app.route : 클라이언트가 요청했을 때 호출될 함수를 등록
@app.route('/')
def index():
    # 클라이언트에게 전달할 데이터를 생성
    html = render_template('index.html')
    # 클라이언트에게 데이터를 전달.
    return html

# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
#app.run(host='0.0.0.0', port = 80)
