from flask import Blueprint, render_template, request
import database

userBlue = Blueprint('user_blue', __name__)

@userBlue.route('/login')
def login():
    html = render_template('user/login.html')
    return html

@userBlue.route('/join')
def join():
    html = render_template('user/join.html')
    return html

@userBlue.route('/modify_user')
def modify_user():
    html = render_template('user/modify_user.html')
    return html

@userBlue.route('/join2', methods = ['POST'])
def join2():
    # 파라미터로 넘어오는 데이터를 추출한다.
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_name, user_id, user_pw)

    # 저장
    database.addUser(user_name, user_pw)

    return '''
            <script>
                alert('가입완룡!! 로그인하기!')
                location.href = '/login'
            </script>
           '''


@userBlue.route('/login2', methods = ['POST'])
def login2() : 
    # 파라미터를 추출한데이
    user_name = request.form.get('user_id')
    # 아까 데이터베이스 설계 때 user_id빼자먹어서 user_name으로 변수명 지정한거임
    # 그런데 login.html에서 파라미터명은 user_id라 안고치고 걍 쓴거임
    user_pw = request.form.get('user_pw')

    # 사용자가 있는지 확인
    row = database.userLogin(user_name, user_pw)
    # print(row)

    if row == None :
        a1 = '''
                <script>
                    alert('아뒤 비번 확인해라 짜샤')
                    location.href = '/login'
                </script>
             '''
    else : 
        a1 = '''
                <script>
                    alert('로그인에 성공!! 환영합니다')
                    location.href = '/'
                </script>
             '''

    return a1
