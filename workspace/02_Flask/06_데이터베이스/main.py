from flask import Flask, render_template, request
import database
import sqlite3
 
app = Flask(__name__, template_folder='view');
 
 
@app.route('/')
def index() :
    html = render_template('index.html')
    return html

@app.route('/insert')
def insert() :
    
    # 저장한다.
    database.insertData('김나은', 28, 36.5)
    database.insertData('추아연', 31, 1.3)
    database.insertData('윤계상', 39, 23.4)
    database.insertData('똘추', 312, 3.34)
    database.insertData('냐옹', 3149, 3.4)

    return '저장완료'

@app.route('/select')
def select() : 
    # 데이터를 가져온다.
    rowList = database.selectData()
    #print(rowList)

    html = render_template('second.html', row = rowList)
    return html

@app.route('/update')
def update():
    # 1번 인덱스에 있는 데이터 수정한다
    database.updateData('변경됐음ㅋ', 1)

    return '수정완.'

@app.route('/delete')
def delete():
    # 데이터 삭제
    # 1번 인덱스 데이터 삭제한다.
    database.deleteData(1)

    return '삭제완'
# 서버를 가동 - 개발용
app.run(debug=True, host='0.0.0.0')
# 서버를 가동 - 서비스용
# app.run(host='0.0.0.0', port=80)
