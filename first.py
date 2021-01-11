import requests
from bs4 import BeautifulSoup as bs
from urls import *
from random import choice 

#from time import sleep

from fake_useragent import UserAgent



def get_html(url, useragent=None, proxy=None):
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text


def get_ip(html):
	print('TRY: new proxy & User-Agent:')
	try:
		soup = bs(html, 'lxml')
		ip = soup.find('span', class_='ip').text.strip()
		ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
		print(ip)
		print(ua)
		print("OK")
	except:
		print('FAILED')
	print("----------------------------------")


def main():
	ip_url = MY_IP_URL

	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')


	html_for_ip = get_html(ip_url)
	get_ip(html_for_ip)

	#ua = UserAgent()

	for i in range (10):
		
		proxy = {'http' : 'http://' + choice(proxies)}
		useragent = {'User-Agent': choice (useragents)}
		#useragent = {'User-Agent': ua.random}

		try:
			html = get_html(ip_url, useragent, proxy)
			get_ip(html )
		except:
			continue

if __name__ == '__main__':
	main()