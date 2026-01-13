import sys, pymysql

#접속
try:
    con = pymysql.connect(host='localhost', 
                          port=3306, 
                          user='root', 
                          password='739458', 
                          database='scrooge',
                          charset='utf8mb4')
    #print(con)
    
    #SQL 실행 객체를 생성
    cursor = con.cursor()
    
    #usertbl_insert_user라는 프로시저를 실행
    cursor.callproc('usertbl_insert_user', ('four123', 'Test123!', '사번', 'four@gmall.com', '01044444444'))
    con.commit()
    
except:
    print("작업 실패\n", sys.exc_info())
    #print("데이터베이스 접속에 실패했습니다.")
    
finally:
    #접속 해제
    if con != None:
        con.close()