#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium 설치
#firefox용 webdrvier 다운로드


# 다음 영화 순위 스크래핑 예제
# http://movie.daum.net/main/new#slide-1-0
# 실시간 예매순위

URL = 'http://movie.daum.net/main/new#slide-1-0'


#firefox를 띄워 브라우저에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#웹브라우저를 자동화할 수 있도록 특수하게 컴파일된 브라우저인 geckodrvier.exe를 다운로드 후 지정한 위치에 저장
driver.get(URL)


# source_code = requests.get(URL)
source_code = driver.page_source    #firefox로 가져온 소스를
                                    #source_code 변수에 저장

rank_list = []          #순위
movietit_list = []      #제목
moviegrd_list = []      #평점
movieopd_list = []      #개봉일


# plain_text = source_code.text
soup = BeautifulSoup(source_code, 'lxml')
# print(soup)
print(soup)

# 순위 추출

for i in range(1,21):
    findkey = "em['class=num_rank rank_" + str(i).zfill(2) + "']"
    print(findkey)
    for r in soup.select(findkey):
        # rank_list.append(r.text.strip().split()[1])
        print(''.join(r.text.strip().split()) )

# 영화 제목 추출
for i in range(1,21):
    findkey = "a['class=link_txt #top #ranking #title @"+ str(i) + "']"
    print(findkey)
    for r in soup.select(findkey):
        print(r.text.strip())
# for i in range(1,21):
#     for r in soup.select("a['class=link_g']"):
#         print(r.text.strip())