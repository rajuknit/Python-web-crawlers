import os
import lxml.html
from lxml import etree
import urllib
from collections import defaultdict as dd
'''
    Author-- Raju Varshney 13228
comment
'''
d=dd(lambda:0)

   
url="http://stackoverflow.com/questions?pagesize=50&sort=newest"
#print(url)
tree = lxml.html.parse(url)
questions = tree.xpath('//div[@class="summary"]/h3')  
for question in questions:
            #print(question)
            print(question.xpath('a[@class="question-hyperlink"]/text()'))
            print(question.xpath('a[@class="question-hyperlink"]/@href'))
          
    
