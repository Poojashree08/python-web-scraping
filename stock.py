import requests
from bs4 import BeautifulSoup

def parseprice():
	url = "https://in.finance.yahoo.com/quote/INR=X?p=INR=X"
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	stock = soup.find("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
	return stock

while True:
	print("the current price is" + str(parseprice()))