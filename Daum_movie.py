#-*- coding: utf-8 -*-
import requests
import bs4
import codecs

# 다음 영화 순위 스크래핑 예제
# http://movie.daum.net/main/new#slide-1-0
# 실시간 예매순위

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
rank_list = []          #순위
movietit_list = []      #제목
moviegrd_list = []      #평점
movieopd_list = []      #개봉일

source_code = requests.get(URL)

plain_text = source_code.text
soup = bs4.BeautifulSoup(plain_text, 'lxml')
# print(soup)


# 순위 추출

for i in range(1,21):
    findkey = "span['class=ico_ranking ico_top" + str(i) + "']"
    for r in soup.select(findkey):
        # rank_list.append(r.text.strip().split()[1])
        rank_list.append(''.join(r.text.strip().split()) )

# 영화 제목 추출
findkey = "a['class=link_g']"
for r in soup.select(findkey):
    movietit_list.append(r.text.strip())
# for i in range(1,21):
#     for r in soup.select("a['class=link_g']"):
#         print(r.text.strip())

# 평점 추출
findkey = "em['class=emph_grade']"
for r in soup.select(findkey):
    # if r.text.strip() == '':
    #     moviegrd_list.append('평점 집계 안 됨')         #-- 문제
    # else:
    moviegrd_list.append(r.text.strip() + '/10')

# 개봉일 추출
findkey = "dl['class=list_state']"
for r in soup.select(findkey):
    movieopd_list.append(r.select('dd')[0].text)

movierankall_list = []

for i in range(0,20):
    movierankall_list.append(rank_list[i])
    movierankall_list.append(movietit_list[i])
    movierankall_list.append(moviegrd_list[i])
    movierankall_list.append(movieopd_list[i])
# print(len(movierankall_list))
# for i in range(0,80):
#     print( ''.join(movierankall_list[i]))

print(''.join(movierankall_list))


# ----- 파일 저장하기 파이썬2
fmt = '%s,%s,%s,%s\n'   #출력 형식 정의
# f = open('movie_rank2.txt', 'w')        #파일을 쓰기 모드로 open
# for i in range(0,20):
#     rank = fmt % (rank_list[i], movietit_list[i], moviegrd_list[i], movieopd_list[i])
    # f.write(rank)
    # 유니코드 문자 저장 시 오류발생!@ - codecs 추천!
    # 파이썬2는 기본적으로 모든 문자를 ascii로 처리
    # 파일에 기록 시 먼저 ascii로 디코딩하기 때문에 오류 발생!

# f.write('hello, python!!\n')          #파일에 내용 쓰기
# f.write('안녕하세요, 파이썬!!\n')
# f.close()                               #파일 작업 종료(필수!)

f = codecs.open('movie_rank2a.txt','w','utf-8')
for i in range(0,20):
    rank = fmt % (rank_list[i], movietit_list[i], moviegrd_list[i], movieopd_list[i])
    f.write(rank)
f.close()
#
#
# # ----- 파일 저장하기(파이썬3)
# try:
#     f = open('movie_rank3.txt','w',encoding = 'utf-8')
#     for i in range(0,20):
#         rank = fmt % (rank_list[i], movietit_list[i], moviegrd_list[i], movieopd_list[i])
#         f.write(rank)
#     f.close()
# except Exception as ex:
#     print(ex)


# ----- 파일 읽어 출력하기 (파이썬2)
#readline : 한 줄 씩 읽어옴(추가적으로 while 필요)
#readlines : 모든 줄을 리스트로 읽어옴 (추가적으로 for 필요)
#read : 파일 내용 전체 읽어옴 - 주로 바이너리 파일 처리
f = codecs.open('movie_rank2a.txt','r','utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt','r','utf-8')
lines = f.readlines()
# print(lines)
for line in lines:
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt','r','utf-8')
data = f.read()
print(data)
f.close()

# ----- 파일 읽어 출력하기 (파이썬3)

# f = open('movie_rank3.txt', 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()
#
# f = open('movie_rank3.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# # print(lines)
# for line in lines:
#     print(line)
# f.close()
#
# f = open('movie_rank3.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

#with ~ as 구문으로 파일 다루기
#파일 작업 시 파일을 열고 닫는 것은 번거로운 일임
#파이썬이 알아서 닫아주면 어떨까? - 편리
with codecs.open('movie_rank2a.txt','r','utf-8') as f:
    data = f.read()
    print(data)

#파일 읽기/쓰기 모드
# r : read (읽기), w : write (쓰기) , t : text (텍스트 파일), b : binary(바이너리파일 : 이미지)
# a : append (추가), + : update(수정)
# 파일모드의 기본값은 : rt