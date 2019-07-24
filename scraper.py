# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:00:03 2019

@author: Supriya
"""

import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://karki23.github.io/Weather-Data/assignment.html") 
root="https://karki23.github.io/Weather-Data/"   
                               
soup = BeautifulSoup(html,"lxml")
links=soup.findAll("a", href=re.compile("([A-Za-z])"))

for link in links:
   l=link['href']
   city_name=""
   for alphabet in l:
       if(alphabet!='.'):
           city_name=city_name+alphabet
       else:
           break
   url=urlopen(root+l)
   soup = BeautifulSoup(url,"lxml")
   table = soup.find("table")
   rows = table.findAll('tr')
   csvfile = open(city_name+".csv",'w',newline='')
   thewriter = csv.writer(csvfile)
   for row in rows:
       csvRow = []
       for cell in row.findAll('th'):
           csvRow.append(cell.get_text())
       for cell in row.findAll('td'):
           csvRow.append(cell.get_text())
       thewriter.writerow(csvRow)
   csvfile.close()