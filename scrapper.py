from bs4 import BeautifulSoup
import requests
from mailSnippet import mail
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
	# Enter email id and password of sender
	sender_address = ""    
	password = ""
	# Enter recepient's email address
	receiver_address = ""
	# Enter target price for the amazon product
	targetPrice = ""
	currentPrice = maxint
	while currentPrice > targetPrice:
		currentPrice = getCurrentPrice(url)
		time.sleep(30)
	message = "The price has been dropped to $%s\n" % currentPrice
	message = message + "Click the link below to view the product\n" + url
	mail(sender_address, password, receiver_address, subject, message)
