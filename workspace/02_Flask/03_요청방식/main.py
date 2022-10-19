from flask import Flask, render_template, request
 
app = Flask(__name__, template_folder='view');
 
 
@app.route('/')
def index() :
    html = render_template('index.html')
    return html
 
@app.route('/a1')
def f1() :
    html = render_template('second.html')
    return html
 
# 요청 방식을 post로 설정한다.
@app.route('/a2', methods=['POST'])
def f2() :
    html = render_template('second.html')
    return html
 
# get과 post 모두를 받아들인다.
@app.route('/a3', methods=['GET', 'POST'])
def f3() :
    print(f'요청방식 : {request.method}')
 
    html = render_template('second.html')
    return html
 
 
# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
# app.run(host='0.0.0.0', port=80)
