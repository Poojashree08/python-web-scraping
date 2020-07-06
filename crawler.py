import requests
from bs4 import BeautifulSoup
import os

url = "https://blog.snappa.com/free-stock-photos/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

links = []

x = soup.select('img[src^="https://cdn.shortpixel.ai/client"]')

for img in x:
	links.append(img['src'])

#for l in links:
#   print(l)

os.mkdir("fine_photos")

for index,img_link in enumerate(links):
        img_data = requests.get(img_link).content
        with open("fine_photos\\" + str(index+1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        