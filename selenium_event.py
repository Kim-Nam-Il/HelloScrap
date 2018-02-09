#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

#탐색할 URL 정의
URL = 'https://kr.investing.com/currencies/'

#웹 브라우저 자동화를 위해 웹 드라이버 초기화
driver = webdriver.Firefox(executable_path= 'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#브라우저를 지정한 URL로 이동시킴
driver.get(URL)

#웹 페이지 오른쪽 '암호화폐'탭의 xpath 정의
alink = driver.find_element_by_xpath('//li[@id="QBS_7"]/a')

#마우스, 단축키 이벤트 처리를 위해 ActionChains 사용
mouse = webdriver.ActionChains(driver)

#해당 링크를 마우스클릭으로 처리하기 위해 move_to_element 사용
#즉, 마우스를 링크로 이동한 다음 클릭
mouse.move_to_element(alink).click().perform()

#클릭 후 보여지는 페이지 내용을 source_code에 저장
source_code = driver.page_source

#웹 페이지 내용을 parsing 하기 위해 bs4로 초기화
soup = BeautifulSoup(source_code, 'html.parser')
# print(soup)
crypcode = ['-btc-usd', '-btc-krw', '-eth-usd']
crypcurcode = ['945629', '940808', '997650']

#출력용 변수
crypcode_list = []
crypcurcode_list = []

#비트코인 별 종류(<a href="/currencies/btc-usd" title="BTC/USD - 비트코인 미국 달러" data-gae="-btc-usd">비트코인/달러</a>)
for i in range(0, len(crypcode)):
    findkey = 'a["data-gae='+ str(crypcode[i]) + '"]'
    for t in soup.select(findkey):
        crypcode_list.append(t.text.encode('utf-8'))


#암호화폐 환율(<td class="lastNum pid-945629-last" id="sb_last_945629">7,787.1</td>)
for i in range(0, len(crypcurcode)):
    findkey = 'td["id=sb_last_' + str(crypcurcode[i]) + '"]'
    for t in soup.select(findkey):
        crypcurcode_list.append(t.text.encode('utf-8'))

for i in range(0, len(crypcode)):
    print('%s, %s' % (crypcode_list[i], crypcurcode_list[i]))


driver.close()