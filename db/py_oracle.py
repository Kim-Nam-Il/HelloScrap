#-*- coding: utf-8 -*-
from cx_Oracle import connect
import os                       #cx_Oracle에서 한글처리를 위해 추가

#파이썬에서 oracle을 사용하려면 먼저, Oracle Instant Client와 부속 파일을 설치해야 함
#1. oracle.com에서 Oracle Instant Client 윈도우 x64 다운로드
#   instant client basic, instant client sqlplus
#   c:\Java 아래에 압축 해제
#2. visual studio 2013 재배포패키지 x64 다운로드
#3. 환경변수 설정
#   ORACLE_HOME, TNS_ADMIN, LD_LIBRARY_PATH, PATH
#4. cx_Oracle 모듈 설치

# os.environ['NLS_LANG'] = '.AL32UTF8'  #오라클 환경변수로 인코딩 설정
os.putenv('NLS_LANG', '.AL32UTF8')

#아이디/비번@디비아이피:포트/오라클SID
conn = connect('hr/hr@192.168.136.128:1521/xe')
print(conn.version)

curs = conn.cursor()

# sql = 'select * from EMPLOYEES'
# curs.execute(sql)
#
# rows = curs.fetchall()
# for row in rows:
#     print(row[0], row[1])
#     #오라클에서는 Dict커서를 공식적으로 지원하지 않음
#
# cols = dict((name,col) for col, name in enumerate(curs.description))
#
# print( cols['EMAIL'], cols['JOB_ID'])
#
# curs.close
#
# curs = conn.cursor()

sql = "select * from ZIPCODE_SEOUL"
curs.execute(sql)

rows = curs.fetchall()
for row in rows:
    print(row[0],row[1],row[2],row[3])

curs.close()
conn.close()

