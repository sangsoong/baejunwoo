'''
표준 모듈
'''

import math, random, time, datetime, json
import numpy
import requests

print(time.time())
print(time.ctime(time.time()))

print(time.strftime('%Y-%m-%d %H:%M:%S %a'))

print(datetime.datetime.now())

today = datetime.datetime.now()
today.year
today.month
today.date()

val = numpy.mean([10, 20, 30, 40, 50])
print(val)

res = requests.get('https://www.naver.com')
print(res.text)