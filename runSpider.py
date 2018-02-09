#-*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy runspider currencySpider.py".split())


#scrapy를 윈도우 상에서 구동하려면
#pycharm 환경에서 cmdline.execute()메서드를 이용하면 된다

#단, 추가설치해야하는 패키지는 pypiwin32