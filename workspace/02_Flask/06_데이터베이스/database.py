import sqlite3

# 데이터베이스 접속 함수
# 데이터베이스 접속한 다음 테이블이 없다면 테이블을 만들어주는 작업을 수행한다
# C:\Users\계정\anaconda3\DLLs 폴더에 sqlite3.dll 파일을 넣어준다.

def getConnection() :
    # sqlite 데이터베이스에 접속한다.
    # 만약 파일이 없다면 생성한다.
    conn = sqlite3.connect('test.db')
    # 경로 설정하고싶으면 conn = sqlite3.connect('06_데이터베이스/test.db')
    
    # 만약 테이블이 없다면 생성한다. 테이블 만드는 쿼리
    # 네개의 컬럼
    # 데이터 타입
    # primary key autoincrement : 1씩 증가하는거
    sql = '''
            create table if not exists TestTable
            (idx integer primary key autoincrement,
            textData text not null,
            intData integer not null,
            doubleData real not null)
    '''
    conn.execute(sql)

    return conn

# 데이터를 저장하는 함수
def insertData(a1, a2, a3):
    # 쿼리문 내에 데이터 3개 들어가니까 애초에 함수에 매개변수 3개 넣음
    # 쿼리문
    sql = '''
            insert into TestTable
            (textData, intData, doubleData)
            values
            (?, ?, ?)
          '''

    # ?에 들어갈 값을 튜플로 생성한다
    args = a1, a2, a3

    #데이터베이스 접속
    conn = getConnection()

    # 쿼리문 실행한다.
    # 첫 번째 : 쿼리문, 두번째 : ?에 들어갈 값
    conn.execute(sql, args)

    # 데이터베이스에게 적용하는 명령 전달
    conn.commit()

    conn.close()

# 데이터를 가져오는 함수
def selectData():
    # 데이터베이스 접속
    conn = getConnection()

    # 쿼리
    sql = 'select * from TestTable'

     # 데이터 접근하는 객체를 추출한다.
    cursor = conn.cursor()
    # 쿼리 실행
    cursor.execute(sql)
    # 결과를 가져온다.
    rowList = cursor.fetchall()

    conn.close()

    return rowList

# 수정하는 함수
def updateData(a1, a2):
    # 데이터베이스 접속
    conn = getConnection()

    # 쿼리문
    sql = '''
            update TestTable
            set textData = ?
            where idx = ?
          '''

    # ?에 들어갈 값 정의
    args = a1, a2
    
    # 쿼리 실행
    conn.execute(sql, args)
    conn.commit()

    conn.close()

# 삭제
def deleteData(a1) :

    # 데이터베이스 접속
    conn = getConnection()

    # 쿼리문
    sql = 'delete from TestTable where idx = ?'
    # execute()함수에 두번째 매개변수는 튜플 형이 들어가야함
    # 그래서 정수타입을 튜플이나 리스트로 형 변환 해조야한다.

    args = [a1]

    conn.execute(sql, args)
    conn.commit()

    conn.close()
    
# conn = getConnection()
# print(conn) # 잘 되나 안되나 테스트 하려고 출력해본거임

# conn.close() # 접속해제(연결 계속 하고있으면 언젠가 연결 안됨/갯수제한 있음)