#-*- coding: utf-8 -*-

#파이썬에서 mysql을 사용하려면 Python 표준 DB API를 지원하는
#MySQL DB모듈을 다운로드 한 후 설치해야함 - PyMySQL 모듈
from pymysql import connect, cursors

#mysql connection 생성
conn = connect(host='192.168.136.128', user='lylace', password='Abcdef_12', db='lylace', charset='utf8')

#connection에서 cursor 생성
curs = conn.cursor()

#sql문 작성 후 실행
sql = 'select * from employees'
curs.execute(sql)

#필요하다면, 실행한 sql로부터 데이터 처리
rows = curs.fetchall()
for row in rows:
    print(row[0], row[1], row[2])
    # print(row['lastName'],row['email'],row['jobTitle'])  #안됨!@

#cursor, connection 닫기
curs.close()
conn.close()

#---사전식 커서 사용
conn = connect(host='192.168.136.128', user='lylace', password='Abcdef_12', db='lylace', charset='utf8')
curs = conn.cursor(cursors.DictCursor)

sql = 'select * from customers where state=%s and city=%s'
curs.execute(sql, ('NY', 'NYC'))

rows = curs.fetchall()
for row in rows:
    print(row['phone'], row['city'], row['state'])

curs.close()
conn.close()

#-- 간단한 CRUD
#-- delete from index_test
#-- insert into index_test values ('lylace','987654')
#-- update index_test set uid = 'rowuina' where uid = 'lylace'
#-- select * from index_test
conn = connect(host='192.168.136.128', user='lylace', password='Abcdef_12', db='lylace', charset='utf8')

curs = conn.cursor()
sql = 'delete from index_test'
curs.execute(sql)

curs.close()
conn.commit() #insert, update, delete 시 필요!

curs = conn.cursor()
# sql = "insert into index_test values ('lylace','987654')"
sql = "insert into index_test values ( %s, %s)"
curs.execute(sql,('lylace','987654'))
curs.close()
conn.commit()

curs = conn.cursor()
# sql = "update index_test set uid = 'rowuina' where uid = 'lylace'"
sql = "update index_test set uid = %s where uid = %s"
curs.execute(sql,('rowuina','lylace'))
curs.close()
conn.commit()


#데이터 조회
curs = conn.cursor(cursors.DictCursor)
sql = "select * from index_test"
curs.execute(sql)

rows = curs.fetchall()
for row in rows:
    print(row['uid'], row['pwd'])

curs.close()
conn.close()