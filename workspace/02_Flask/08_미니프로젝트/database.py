import sqlite3

def getConnection() :

    # 데이터베이스 열어줌
    conn = sqlite3.connect('mini.db')

    sql = '''
            create table if not exists UserTable
            (user_idx integer primary key autoincrement,
             user_name text not null,
             user_pw text not null)
          '''
    conn.execute(sql)

    return conn

# 회원 데이터 저장
def addUser(user_name, user_pw) :

    # 데이터베이스 접속
    conn = getConnection()

    # z쿼리문
    sql = '''
            insert into UserTable
            (user_name, user_pw)
            values
            (?, ?)
          '''

    args = user_name, user_pw

    conn.execute(sql, args)
    conn.commit()
    conn.close()


# 로그인 처리
def userLogin(user_name, user_pw) : 

    conn = getConnection()
    cursor = conn.cursor()

    sql = '''
            select * from UserTable
            where user_name = ? and user_pw = ?
          '''

    args = user_name, user_pw

    cursor.execute(sql, args)

    row = cursor.fetchone()

    conn.close()
    
    return row