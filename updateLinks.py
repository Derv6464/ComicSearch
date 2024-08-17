import getAllLinks

def getFullUpdate():
    c = open("lastLink.txt","w")
    c.write(getAllLinks.charLinks("https://marvel.fandom.com/wiki/Category:Characters",True))
    c.write(getAllLinks.comicLinks("https://marvel.fandom.com/wiki/Category:Comics",True))
    c.write(getAllLinks.charNoEarthLinks("https://marvel.fandom.com/wiki/Category:Disambiguation_Pages",True))

    c.close() 

def getNewUpdate():
    c = open("lastLink.txt","r")

    dataIn = c.read()
    finalLinks = dataIn.split("\n")
    c.close()

    c = open("lastLink.txt","w")
    c.write(getAllLinks.charLinks(finalLinks[0],False))
    c.write(getAllLinks.comicLinks(finalLinks[1],False))
    c.write(getAllLinks.charNoEarthLinks(finalLinks[2],False))

    c.close() 


    
