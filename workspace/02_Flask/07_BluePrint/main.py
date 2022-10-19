from flask import Flask, render_template, request
from blue1 import blue100
from blue2 import blue200
 
# blueprint는 파일을 분리해가지고
# 블루프린트 객체를 생성해가지구 임포트해서 블루프린트 등록하면된다고..
# main.py 파일이 좀 가벼워진다
# 파일을 나눠서 관리 할 수 있다


app = Flask(__name__, template_folder='view') # view 폴더를 지정해놨음

# blueprint 등록
app.register_blueprint(blue100)
app.register_blueprint(blue200)
 
 
@app.route('/')
def index() :
    html = render_template('index.html') # 위에 view폴더에서 index.html을 찾겠다
    return html

# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
# app.run(host='0.0.0.0', port=80)
