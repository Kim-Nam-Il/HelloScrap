
# 설치 필수 패키지
# requests
# BeautifulSoup
#
# 파이썬 패키지 설치 방법
# 1 미리 설치하고 작업 : pip 패키지 관리자
# 2 작업 중 설치 : alt + enter

import requests
import bs4
#py3에서는 bs4로 설치
#py2에서는 BeautifulSoup로 설치

# 지정한 URL로부터 HTML소스를 가져옴
source_code = requests.get('http://naver.com')
# source_code.encoding = 'euc-kr'

# 웹사이트에서 HTML 소스를 출력함 - 보기 불편
# print(source_code.text)

# 지정한 웹페이지 소스를 변수에 저장
plain_text = source_code.text

# 웹 소스를 보기 좋게 변환 (lxml 이용)
soup = bs4.BeautifulSoup(plain_text, 'lxml')
print(soup)

# 웹 소스를 단순히 파싱
# soup = bs4.BeautifulSoup(plain_text, 'html.parser')
# print(soup)

for title in soup.select('title'):
    print(title.text)

for title in soup.select('h3'):
    print(title.text)

for title in soup.select("h3['class=tit']"):
    print(">>>" + title.text)