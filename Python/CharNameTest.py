from bs4 import BeautifulSoup
import requests
url = "https://marvel.fandom.com"
url2 = "https://marvel.fandom.com/wiki/Yelena_Belova_(Earth-616)"
url3 = "https://marvel.fandom.com/wiki/Ruth_Goldman_(Earth-616)"
link1="/wiki/Barbara_Rave_(Earth-616)"
link2="/wiki/Natalia_Romanova_(Earth-616)"
link3="/wiki/Robyn_Hood_(Earth-616)"
link4="/wiki/Agent_of_Hell_(Earth-616)"
link5="/wiki/%C3%98de_(Earth-616)"
link6="/wiki/Jamie_(Mutant)_(Age_of_X-Man)_(Earth-616)"


r = requests.get(url+link6)
soup = BeautifulSoup(r.content, 'html.parser')
name = soup.findAll('div', class_="pi-data-value pi-font")
NAME = name[0].getText()

if "Current Alias" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[1]:
    curAlias = name[1].getText()
else:
    curAlias=""

if "Alias" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[2] or "Aliases" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[2]:
    AliasN = name[2].getText()
    aSplit1 = AliasN.split(",")
    aSplit2 = []
    for i in aSplit1:
        aSplit2.append(i.split("]"))

    alias = []
    for i in aSplit2:
        for j in i:
            if "[" in j or "]" in j:
                pass
            else:
                alias.append(j)
elif "Alias" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[1] or "Aliases" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[1]:
    AliasN = name[1].getText()
    aSplit1 = AliasN.split(",")
    aSplit2 = []
    for i in aSplit1:
        aSplit2.append(i.split("]"))

    alias = []
    for i in aSplit2:
        for j in i:
            if "[" in j or "]" in j:
                pass
            else:
                alias.append(j)
else:
    alias=[]


    
print("name")
print(NAME)
print("cur alias")
print(curAlias)
print("all alias")
for i in alias:
    print(i)


