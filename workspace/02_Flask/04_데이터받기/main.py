from flask import Flask, render_template, request
 
app = Flask(__name__, template_folder='view');
 
 
@app.route('/')
def index() :
    html = render_template('index.html')
    return html

# get 방식
# 모든 데이터는 주서에 붙어서 오기 때문에 공개된다.
# 데이터의 총 길이가 255글자가 넘어가면 잘린다.
# 전송 속도가 빠르다

@app.route('/a1')
def a1() :
    #get방식으로 넘어오는 데이터는 args라는 이름의 딕셔너리로 전달됨
    #print(request.args)
    
    # 파라미터로 넘어오는 값을 추출한다.
    v1 = request.args.get('v1')
    v2 = request.args.get('v2')
    return f'v1 : {v1}, v2 : {v2}'


# post 방식
# 모든 데이터는 header라는 영역에 숨겨져서 전달됨
# 데이터의 글자 길이의 제한이 읎당.
# 전송 데이터의 용량이 커지기 땜에 전송 속도가 get보다 느리다.(사실 별 차이 읎삼)
# form이라는 것을 통해 추출한다.

@app.route('/a2', methods = ['POST'])
def a2() :
    # print(request.form)
    
    # 파라미터로 넘어오는 값을 추출한다.
    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    return f'data1 : {data1}, data2 : {data2}'
 
# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
# app.run(host='0.0.0.0', port=80)
