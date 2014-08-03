'''
Created on 2014年8月3日

@author: Terry
'''

from bs4 import BeautifulSoup
import urllib.request
import re

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

f= urllib.request.urlopen("http://www.lecai.com/lottery/jczq/")

doc = f.read()

soup = BeautifulSoup(doc)

#print(soup)

#a = soup.find_all('id','m_2014080301014');
a = soup.findAll('td')

print(a)

