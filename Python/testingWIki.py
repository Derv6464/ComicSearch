from bs4 import BeautifulSoup
import requests
url = "https://marvel.fandom.com/wiki/Category:Characters?from=Wade+Wilson+%28Earth-000000000014031%29%0AWade+Wilson+%28Earth-14031%29"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
nextLink = soup.find('div', class_='category-page__pagination')
nxtLnk = []
for j in nextLink.findAll('a'):
    nxtLnk.append(j.get('href'))
    
print(nxtLnk)