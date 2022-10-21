from flask import Flask, render_template, request
import os # main.py가 실행되는 위치를 가져옴

import pickle
import pandas as pd
import numpy as np

from tensorflow.keras.models import load_model

app = Flask(__name__, template_folder='view')
 
@app.route('/')
def index() :
    html = render_template('index.html')
    return html
 
@app.route('/result', methods=['POST'])
def result() :

    # upload라는 이름의 input type = file 이 있는지 검사
    if 'upload' in request.files : 
        # 업로드된 파일을 가져온다.
        file_data = request.files['upload'] # index.html에 들어있는 파라미터 이름임
        # 저장한다
        file_data.save(f'upload/{file_data.filename}') # upload폴더에 저장시킴

        ### 이렇게 주피터에서 쓰던 코드 그대로 활용할 수 있다
        ### 이 말인 즉슨 웹에서 가져온 데이터를 가지고 학습을 할 수도 있다는 말임 ㄷㄷ

        # 학습 모델등을 복원한다.
        model = load_model('model/03_model.h5')

        with open('model/train_model2.dat', 'rb') as fp :
            encoder_dict = pickle.load(fp)
            scaler1 = pickle.load(fp)


        #print(encoder_dict)
        #print(scaler1)
        #print(model)

        # 데이터 불러온다
        df1 = pd.read_csv(f'upload/{file_data.filename}')
        # print(df1) 불러온거 확인

        # 컬럼 목록을 가져온다
        columns = df1.columns

        # 숫자로 변환한다
        for c1 in columns :
            encoder1 = encoder_dict[c1]
            df1[c1] = encoder1.transform(df1[c1])

        # 표준화
        X = scaler1.transform(df1)
        # print(X)

        # 예측
        pred = model.predict(X)

        # 환산한다
        pred = (pred >= 0.5).astype('int')
        pred = pred.reshape(-1)

        result = encoder_dict['class'].inverse_transform(pred)
        print(result)


    html = render_template('result.html', result=result, enumerate = enumerate)
    # enumerate함수를 변수로 만들어서 html에 사용가능함
    return html
 
app.run(debug=True, host='0.0.0.0')

