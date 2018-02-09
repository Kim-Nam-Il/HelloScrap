import requests
import bs4

#다음 JTBC 뉴스 스크래핑 예제
#http://media.daum.net/cp/310?page=2&regDate=20170501&cateId=1001

press = [310]       #언론사
date = [20180205]   #연월일
page = [1,2,3]      #페이지

new_title = []      #뉴스 제목
new_desc = []       #뉴스 간략소개

#스크래핑할 URL 지정
URL = 'http://media.daum.net/cp/' + str(press[0]) + '?page=' + str(page[0]) + '&regDate=' + str(date[0])

#스크래핑해서 소스를 source_code에 저장
source_code = requests.get(URL)

#중간 결과 출력
# print(source_code.text)

#텍스트 추출을 위해 lxml로 태그 분석(메모리 적재)
plain_text = source_code.text
soup = bs4.BeautifulSoup(plain_text, 'lxml')

#기사 제목 추출
cnt = 1
for title in soup.select("a['class=link_txt']"):
    if cnt > 15:
        break
    new_title.append(title.text.strip())
    cnt += 1


#기사 미리보기 추출
cnt = 1
for title in soup.select("span['class=link_txt']"):
    if cnt > 15:
        break
    new_desc.append(title.text.strip())
    cnt += 1


#기사 제목 및 미리보기 출력
articleboth_list = []
for i in range(0,15):
    articleboth_list.append(new_title[i] +'\n')
    articleboth_list.append(new_desc[i])
    articleboth_list.append('\n\n')

print(''.join(articleboth_list))
