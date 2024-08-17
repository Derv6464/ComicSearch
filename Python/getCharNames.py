from bs4 import BeautifulSoup
import requests
d = open("nameChar.csv","w")
c = open("curAlias.csv","w")
a = open("allAlias.csv","w")
f = open("616Char.csv","r")
dataIn = f.read()
list1 = dataIn.split("\n")
url = "https://marvel.fandom.com"
p = 0
list1.remove('/wiki/Jamie_(Mutant)_(Age_of_X-Man)_(Earth-616)')
for k in list1:
    r = requests.get(url+k)
    soup = BeautifulSoup(r.content, 'html.parser')
    name = soup.findAll('div', class_="pi-data-value pi-font")
    if name:
        NAME = name[0].getText()
        if "[" in NAME:
            NAME.split("[")
            NAME = NAME[0]

        if "Current Alias" in soup.findAll('h3', class_="pi-data-label pi-secondary-font")[1]:
            curAlias = name[1].getText()
            if "[" in curAlias:
                curAlias.split("[")
                curAlias = curAlias[0]
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

        if NAME:
            d.write(k+","+NAME+"\n")
        if curAlias:
            c.write(k+","+curAlias+"\n")
        if alias:
            for l in alias:
                a.write(k+","+l+"\n")
        if p%50 == 0:
            print(p,k,NAME)
        p+=1
    else:
        pass
f.close()
d.close()
c.close()
a.close()