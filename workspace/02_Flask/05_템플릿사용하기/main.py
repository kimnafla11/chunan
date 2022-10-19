from flask import Flask, render_template, request
 
app = Flask(__name__, template_folder='view');
 
 
@app.route('/')
def index() :

    # data_dic : html문서를 구성하기 위해 필요한 데이터가 담긴 딕셔너리를 설정함
    # data_list : html문서를 구성하기 위해 필요한 데이터가 담긴 리스트를 설정함

    test_dic = {
        'a1' : 28,
        'a2' : '김나은'
    }

    test_dic2 = {
        'a3' : '추아연',
        'a4' : '븅신ㅋㅋ'
    }

    test_list = ['야','임마',36,230,2]

    # 두번째부터... : 두번째부터는 ** 가변형 매개변수로 받는다
    # html 파일을 작성할 때 이름을 이용하여 html문서에서 사용하면 덴다.
    html = render_template('index.html', data_dic = test_dic, data_list = test_list, data_dic2 = test_dic2)
    return html

# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
# app.run(host='0.0.0.0', port=80)
