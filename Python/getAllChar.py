from bs4 import BeautifulSoup
import requests
d = open("AllChars.csv","w")           #opening file to write links in
url = "https://marvel.fandom.com/wiki/Category:Characters"

#url2 = "https://marvel.fandom.com/wiki/Category:Comics?from=%C2%A019420601All+Winners+Comics+Vol+1+5%0AAll+Winners+Comics+Vol+1+5"
allAllLink = []                       #defining list for links to character go in
i = 0
allLnk = []
while url:     #seeting up while loop

#for i in range(50):
    
    if i%10 == 0:
        print(i)
        print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    nextLink = soup.find('div', class_='category-page__pagination')
    results = soup.find('div', class_='category-page__members')


    allLink = []
    for link in results.findAll('a'):
        allLink.append(link.get('href'))
    
    
    allLink = list(dict.fromkeys(allLink))
    for a in allLink:
        allAllLink.append(a)

    nxtLnk = []
    
    for j in nextLink.findAll('a'):
        nxtLnk.append(j.get('href'))
    if i == 0:
        url = nxtLnk[0]
    elif i == 1:
        url = nxtLnk[1]
    #elif i >= 350:
    #    print(i)
    #    print(nxtLnk[2])
    #elif i == 361:
    #    break
    elif nxtLnk[1] == "https://marvel.fandom.com/wiki/Category:Characters?from=Zarek+%28Earth-000000000079102%29%0AZarek+%28Earth-79102%29":
        url = ""
    else:
        url = nxtLnk[2]
        
    #while i >= 340:
    #    print(i)
    #    print(nxtLnk+"/n"+nxtLnk[2]+"/n")
    i += 1
    allLnk.append(url)
    
    
allAllLink = list(dict.fromkeys(allAllLink))
#for i in range(22):
#    del allAllLink[0]


#writng into file 
for a in allAllLink:
#for a in allLnk:
    #print(a)
    d.write(a + "\n")
    
d.close()