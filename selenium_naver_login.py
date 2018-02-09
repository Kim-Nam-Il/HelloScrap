#-*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#탐색할 URL 정의
URL = 'https://www.naver.com'

#웹 브라우저 자동화를 위해 웹 드라이버 초기화
driver = webdriver.Firefox(executable_path= 'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#브라우저를 지정한 URL로 이동시킴
driver.get(URL)

#로그인창에 아이디/비번 입력 후 로그인 버튼 클릭

#html요소 중 id가 id인 요소를 찾음
userid = driver.find_element_by_id('id')

#@id=id 인 요소에 아이디를 입력
userid.send_keys('skchang8')

#html요소 중 id가 pw인 요소를 찾음
userpw = driver.find_element_by_id('pw')

#@id=pw인 요소에 비밀번호를 입력
userpw.send_keys('')

#로그인버튼을 찾아 클릭
loginbtn = driver.find_element_by_xpath('//input[@title="로그인"]')
loginbtn.submit()

#처리속도가 빨라서 로그인완료 페이지가 뜨기 전에
#메일 페이지로 이동하기 때문에 지연시간을 둬야함
#(서버로부터 넘어오는 응답데이터를 받을 때까지)
#일정시간 동안 브라우저 대기
# driver.implicitly_wait(3)
time.sleep(3)           #파이썬 처리 지연

#메일 페이지로 이동
MailURL = 'https://mail.naver.com/'
driver.get(MailURL)

#페이지 내용을 source_code에 저장
source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')

#안 읽은 메일 (span[class=cnt], //span[@class="cnt"]
findkey = 'span["class=cnt"]'
for t in soup.select(findkey):
    print(t.text)

#로그아웃버튼 클릭 - 로그아웃 처리 (//*[@id="gnb_logout_button"])
# time.sleep(3)
# mouse = webdriver.ActionChains(driver)
# logoutbtn = driver.find_element_by_xpath('//span[@id="gnb_name1"]')
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
# logoutbtn = driver.find_element_by_xpath('//a[@id="gnb_logout_button"]')
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
# driver.get('http://naver.com')
#버튼이 아닌 링크인 경우 클릭 안 먹힐 때가 있음

#로그아웃 페이지 가기 - 로그아웃 처리
logoutURL = 'https://nid.naver.com/nidlogin.logout?/returl=https://naver.com'
driver.get(logoutURL)

driver.close()