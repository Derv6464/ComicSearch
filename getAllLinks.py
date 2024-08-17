#this gets the links to each page of every comic on marvel.fandom.com

from bs4 import BeautifulSoup
import requests

#character links
def charLinks(url,f):
    if f:
        d = open("txt/characterLinks.txt","w")           #opening file to write links in
    else:
        d = open("txt/characterLinks.txt","a")           #openign file to append links in
    allAllLink = []                       #defining list for links to go in
    i = 0
    while url:                            #seeting up while loop
    #for i in range(100):
        
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
        elif len(nxtLnk)==2:
            
            break
        else:
            url = nxtLnk[2]
        i += 1
        
        
        
    allAllLink = list(dict.fromkeys(allAllLink))

    return(nxtLnk[1])     
    for a in allAllLink:
        d.write(a + "\n")
       
    d.close()

#comic links
def comicLinks(url,f):
    if f:
        d = open("comicLinks.txt","w")           #opening file to write links in
    else:
        d = open("comicLinks.txt","a")
    allAllLink = []                       #defining list for links to go in
    i = 0
    while url:                            #seeting up while loop
    #for i in range(100):
        
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
        elif len(nxtLnk)==2:
            break
        else:
            url = nxtLnk[2]
        i += 1
        
        
        
    allAllLink = list(dict.fromkeys(allAllLink))

    return(nxtLnk[1])   
    for a in allAllLink:
        d.write(a + "\n")
        
    d.close()

#characters without the earth they are from
def charNoEarthLinks(url,f):
    if f:
        d = open("characterLinks.txt","w")           #opening file to write links in
    else:
        d = open("characterLinks.txt","a")
    allAllLink = []                       #defining list for links to go in
    i = 0
    while url:                            #seeting up while loop
    #for i in range(100):
        
        #if i%10 == 0:
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
            url = nxtLnk[2]
        elif len(nxtLnk)==2:
            break
        else:
            url = nxtLnk[2]
        i += 1

        
        
        
    allAllLink = list(dict.fromkeys(allAllLink))

    return(nxtLnk[1])     
    for a in allAllLink:
        d.write(a + "\n")
        
    d.close()

