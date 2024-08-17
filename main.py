import updateLinks
import cleanLinks

print("Do you want to full update[1] or only get new links[2]?")
option = int(input())

if option == 1:
    updateLinks.getFullUpdate()
else:
    updateLinks.getNewUpdate()
    
cleanLinks.cleanCharacter()
cleanLinks.cleanComic()
cleanLinks.cleanNoEarthChars()