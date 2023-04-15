from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(START_URL)
print (page)
soup = BeautifulSoup(page.text, "html.parser")
starTable=soup.find("table")
temp_list=[]
table=starTable.find_all("tr")
for tr in table:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
starName=[]
starMass=[]
starDistance=[]
starRadius=[]
for i in range(1,len(temp_list)):
    starName.append(temp_list[i][1])
    starDistance.append(temp_list[i][3])
    starMass.append(temp_list[i][5])
    starRadius.append(temp_list[i][6])
df2=pd.DataFrame(list(zip(starName,starDistance,starMass,starRadius)),columns=["name",'distance','mass','distance'])
df2.to_csv("stars.csv")
