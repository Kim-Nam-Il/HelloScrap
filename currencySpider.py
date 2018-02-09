#-*- coding: utf-8 -*-
import scrapy
import codecs
import sys
#리눅스 상에서 파이썬2를 이용해서 utf-8로
#파일에 내용을 기록하려면
#시스템 기본 인코딩을 utf-8로 설정해야 함
reload(sys)
sys.setdefaultencoding('utf8')


#scrapy에서 spider는 크롤링/스크래핑을 담당하는 핵심부분
#크롤링/스크래핑 절차에 대한 정의를 하는 부분
class CurrencySpider(scrapy.Spider):
    name = 'currencySpider'        #스파이더 프로그램 이름 정의
    start_urls = ['http://finance.naver.com/marketindex/?tabSel=exchange#tab_section']
                        #스파이더가 스크래핑할 위치를 URL로 정의

    def parse(self, response):
        #start_urls에 정의된 URL을 스파이더가 스크래핑하고
        #내용이 다운로드 된 후 호출되는 메서드
        #parse()는 실제 추출할 데이터를 작업한 후 결과로
        #결과를 return 하는 역할 담당

        currencies = response.css('.blind::text').extract()

        values = response.css('.value::text').extract()

        currency_list = []
        value_list = []

        with codecs.open('exchange_rates.csv','w','utf-8') as f:
            #처리결과를 파일에 저장하기 위해
            #movierank.csv라는 이름, 쓰기 모드로 open

            for i in range(0,16,3):
                currency = currencies[i].replace('\r\n','')
                    #/r/n -> whitespace
                currency = currency.strip().encode('utf-8')
                    #빈칸으로 분리 후 다시 합침
                currency_list.append(currency)

            for i in range(0,4):
                value = values[i].replace('\r\n','')
                value = value.strip().encode('utf-8')
                    # utf-8로 변환 후 출력
                value_list.append(value)

            for i in range(0,4):
                print('%s,%s\n' % (currency_list[i],value_list[i]))
                f.write('%s,%s\n' % (currency_list[i], value_list[i]))
                #파일에 기록

        f.close()