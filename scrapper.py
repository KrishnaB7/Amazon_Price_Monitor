from bs4 import BeautifulSoup
import requests
import time
from sys import maxint


def getCurrentPrice(url):
	html_page = requests.get(url).text
	soup = BeautifulSoup(html_page,'lxml')
	if soup.find(id="priceblock_ourprice"):
		soup = soup.find(id="priceblock_ourprice")
	else:
		soup = soup.find(id="priceblock_dealprice")
	if soup == None:
		return 0
	soup = soup.string
	return float(soup[1:])



if __name__ == '__main__':
	url = 'https://www.amazon.com/i37-Headphones-Children-Adjustable-Cellphones/dp/B07DJ1WFM1/ref=gbps_img_s-5_779e_7da4b254?smid=A278Y5EX1FT7TL&pf_rd_p=51a6201c-895a-4312-82ad-229c1f8e779e&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=R79QDFYKBR4547FHGNYP'
	targetPrice = 12.00
	currentPrice = maxint
	while currentPrice > targetPrice:
		currentPrice = getCurrentPrice(url)
		# Wait for 5 seconds
		time.sleep(5)
		print currentPrice





#id="priceblock_dealprice"
#<span id="priceblock_ourprice" class="a-size-medium a-color-price">$38.90</span>