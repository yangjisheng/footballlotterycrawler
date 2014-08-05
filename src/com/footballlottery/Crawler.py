'''
Created on 2014年8月3日

@author: Terry
'''

from bs4 import BeautifulSoup
import urllib.request
import json
import time
import re
from string import Template

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
#----------------------------------------------乐彩数据采集网址-----------------------------------------------
# http://www.lecai.com/include/static/odds_jczq/80/euro/jczq_20140805.json
# http://www.lecai.com/include/static/odds_jczq/80/vs_20140805.json
# http://data.lecai.com/football/match/oddsEuro.do?id=1260455&action=oddsEuroDetail&bookmakerId=40&isEx=0
# http://data.lecai.com/football/match/oddsEuro.do?id=1260455
#http://data.lecai.com/football/match/oddsEuro.do?id=1252361&action=widget&page=1&size=303&filter= 百家欧赔的json串
# f= urllib.request.urlopen("http://www.lecai.com/lottery/jczq/")
#--------------------------------------------------------------------------------------------------------

doc = urllib.request.urlopen("http://www.lecai.com/include/static/odds_jczq/80/euro/jczq_20140805.json")

jsonstr = BeautifulSoup(doc)

# print(jsonstr)

s = json.loads(str(jsonstr))

# print(s.keys())
# print(len(s.keys()))

for key in s:
    link = "http://data.lecai.com/football/match/oddsEuro.do?id="+key
    d = urllib.request.urlopen(link)
    soup = BeautifulSoup(d.read())
    totalstr=soup.find(class_="info_box")
    #将欧赔公司总数正则出来 例： 共【306】家欧赔公司 取306 放入百家欧赔json串链接中
    pattern = re.compile(r'【\d*】')
    


   



