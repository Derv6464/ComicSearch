#https://marvel.fandom.com/wiki/Immortal_X-Men_Vol_1_3
# https://marvel.fandom.com/wiki/Excalibur_Vol_4_2
#/wiki/Chili_Vol_1_17
import getTestLinks
import requests
from bs4 import BeautifulSoup
import time
import re
start = time.time()
f = open("csv/comicLinksClean.csv","r")
d = open("csv/feat.csv","w")
s = open("csv/supp.csv","w")
o = open("csv/other.csv","w")
a = open("csv/antag.csv","w")

dataIn = f.read()
list1 = dataIn.split("\n")

#url = '/wiki/Homer^_the_Happy_Ghost_Vol_1_2'
#urls = getTestLinks.getRand(1)
for k in range(len(list1)):
#for i in range(1):
    
    types = {
    'Featured Characters:': '',
    'Supporting Characters:' :'' ,
    'Other Characters:' : '',
    'Antagonists:' : '',
    'Vilians:':'',
    
    }
    if "^" in list1[k]:
        list1[k] = list1[k].replace("^",",")
    #print("https://marvel.fandom.com" + list1[i])
    r = requests.get("https://marvel.fandom.com" + list1[k])        #get link
    soup = BeautifulSoup(r.content, 'html.parser')       #get web contents
    results = soup.find('div', class_='mw-parser-output')    #getting ceratin part of website
    bruh = str(results)
    text2 = ''.join(bruh.split())
    searchtxt = text2.split('<h2style="text-align:left">')

    starts = ['Antagonists:','Other Characters:','Featured Characters:','Supporting Characters:','Vilians:'] #all options that the file could start wiht
    ends = ['Races and Species:','Locations:','Items:','Vehicles:']    #all options the file could end with
    order = list(results.findAll('b'))       #getting the headings (in bold)

    for i in range(len(order)):
        order[i] = str(order[i].get_text()) #getting text from the html files
        

    notOrder = []
    for i in order:
        if i not in starts and i not in ends:        #get anything in bold isnt in the given list 
            notOrder.append(i)
    
    #should be the same - need to test
    #notOrder = [i for i in order if i not in starts and i not in ends]
    
    order = [i for i in order if i not in notOrder]          #get rid of anything not in given list

    if len(order)<1:
        print("skipped",list1[k])      #skip if page is empty
        continue

    volNum = []
    linkFeat = []
    texts = []
    
    if len(order) < 2:          #if only one heading
        runs =1
    else:
        runs =len(order)-1

    for i in range(runs):
        if order[i] in ends:                #break if its in ends/ got data i want
            break
        else:
            split2 = bruh.split(order[i])
            if len(order) < 2:
                split3 = feat2[1].split('Synopsis')
                
            else:
                split3 = feat2[1].split(order[i+1])
            split4 = BeautifulSoup(feat3[0], 'html.parser')
            
            for link in split4.findAll('a'):      #get all links in the featured section
                links.append(link.get('href'))
            for j in range(links.count(None)):   #removes any null values
                links.remove(None)
            for j in range(len(links)):    #gets rid of any links that link to another comic
                if "Vol" in links[j]:
                    volNum.append(j)
                else:
                    pass
            links = [l for j, l in enumerate(links) if j not in volNum] 
            
            types[order[i]] = links
            links = []

    for i in types['Featured Characters:']:
        d.write(str(k) +"," + i + "\n")
    for i in types['Supporting Characters:']:
        d.write(str(k) +"," + i + "\n")
    for i in types['Other Characters:' ]:
        d.write(str(k) +"," + i + "\n")
    for i in types['Antagonists:']:
        d.write(str(k) +"," + i + "\n")
    for i in types['Vilians:']:
        d.write(str(k) +"," + i + "\n")
        
            
    if k%10 == 0:
        curTime = time.time()
        curElapsed = curTime-start
        print(curElapsed)
        print(curElapsed/60)
        print(k)

stop = time.time()
elapsed = stop-start
print(elapsed)
print(elapsed/60)
print(elapsed/60/60)




        
        