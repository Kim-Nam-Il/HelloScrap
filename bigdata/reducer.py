#-*- coding: utf-8 -*-
import sys
import codecs

#파이썬으로 작성해보는 맵리듀스 구현 예제
#워드카운트 - 파일에 작성된 단어 빈도를 계산 후 출력

sys.stdin = codecs.open('mapresult.txt', 'r', 'utf-8')
#맵 단계에서 처리한 결과가 들어 있는 파일을 읽어옴

word2count = {}
#리듀스한 중간/최종 결과를 저장하기 위해 dict 자료구조 이용

for line in sys.stdin:                  #파일의 내용을 한 줄씩 읽어서
    cline = line.strip()                #라인의 앞뒤 공백 제거
    word, count = cline.split('\t', 1)  #탭으로 구분해서
                                        #2개의 항목으로 분리 각각을 word, count에 저장

    try:
        count = int(count)              #문자값인 count를 숫자로 변환
    except ValueError:
        continue                        #오류 발생 시 계속 진행(공백인 경우)

    try:
        word2count[word] = word2count[word] + count
        #dict 자료구조에 문자와 출현빈도를 저장
        #문자는 키로, 출현빈도는 값형태로 처리
        #만일 기존에 저장된 문자가 있다면
        #그 문자의 출현빈도에 합산 처리
    except:
        word2count[word] = count
        #dict 자료구조에 문자와 출현빈도를 저장할 때
        #오류가 발생하면 문자, 출현빈도는 키와 값으로 저장
        #문자키로 검색했는 데 값이 존재하지 않으므로@!

    # print(word2count)
    #리듀스 중간처리 결과 확인

for word in word2count.keys():
    #word2count에 저장된 모든 키를 하나씩 읽어와서
    print('%s\t%s' % (word, word2count[word]))
    #그 키에 해당하는 값을 출력