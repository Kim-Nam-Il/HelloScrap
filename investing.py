#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium 설치
#firefox용 webdrvier 다운로드

URL = 'https://kr.investing.com/currencies'
#firefox를 띄워 브라우저에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#웹브라우저를 자동화할 수 있도록 특수하게 컴파일된 브라우저인 geckodrvier.exe를 다운로드 후 지정한 위치에 저장
driver.get(URL)


# source_code = requests.get(URL)
source_code = driver.page_source    #firefox로 가져온 소스를
                                    #source_code 변수에 저장
soup = BeautifulSoup(source_code, 'lxml')

currid = [1,2,3,125,5,6,7,8,650,159]    #종목번호

#종목 추출
findkey = 'td["class=left noWrap"]'
for t in soup.select(findkey):
    print(''.join(t.text.strip().split()))


#현재가 추출
for i in range(0, len(currid)):
    findkey = 'td["class=pid-"' + str(currid[i]) + '"-last"]'
    for t in soup.select(findkey):
        print(''.join(t.text.strip().split()))
