from bs4 import BeautifulSoup
import requests
import csv
f = open("ComicNumToLinkMake.csv","r")
l = open("ComicNumToLinkToName.csv","w")
list1 = []
line_count = 0
csv_f = csv.reader(f)
for row in csv_f:
    if line_count>=0:
        list1.append(row)
    line_count = line_count + 1
url = "https://marvel.fandom.com"
for k in list1:
    r = requests.get(url+k[1])
    soup = BeautifulSoup(r.content, 'html.parser')
    name = soup.find('h1', class_="page-header__title")
    if name:
        l.write(k[0]+","+k[1]+","+(name.getText()).lstrip()+"\n")
    else:
        pass
    if int(k[0])%25==0:
        print(k[0]+","+k[1]+","+(name.getText()).lstrip()+"\n")
        
f.close()
l.close()