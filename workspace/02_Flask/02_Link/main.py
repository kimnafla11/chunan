from flask import Flask, render_template

# 서버 객체 생성
# 첫 번째 : 아무 문자열을 넣어준다.
app = Flask(__name__, template_folder='view')

# / : 주소만 입력해서 요청한 경우
@app.route('/')
def index():
    html = render_template('index.html')
    return html

# second : 주소 뒤에 second를 붙여서 요청한 경우
@app.route("/second")
def second():
    html = render_template('second.html')
    return html

# third : 주소 뒤에 third를 붙여서 요청한 경우
@app.route("/third")
def third():
    html = render_template('third.html')
    return html

# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
#app.run(host='0.0.0.0', port = 80)
