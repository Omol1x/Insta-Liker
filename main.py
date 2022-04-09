#Позаимствовал NETSCAPE to JSON у lolz.guru/members/2977610
#Свежая версия chromedriver - bit.ly/35PexKM
#Мой лолз - lolz.guru/market/28417127

import requests, os, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from convert import main_convert
from multiprocessing import Pool

'''Settings'''
link = 'https://www.instagram.com/p/CAfWIHknY-9/' #Ссылка на фото
threading = 10 #Количество потоков

'''Do not change'''
path = os.path.abspath(os.curdir)+'\\cookies'
pathtochrome = os.path.abspath(os.curdir)+'\\chromedriver.exe'
elements = []

'''Main function'''
def main(i):
	try:
		os.chdir(path)
		with open(i) as json_file:
			cookies = json.load(json_file)
		driver = webdriver.Chrome(executable_path=pathtochrome)
		driver.get(url=link)
		for c in cookies:
			driver.add_cookie(c)
		driver.refresh()
		sleep(4)
		driver.find_elements_by_tag_name('button')[2].click()
	except Exception as e:
		print(e)

'''Starting'''
if __name__ == '__main__':
	main_convert()
	for i in os.listdir(path):
		if '.json' in i:
			elements.append(i)
	with Pool(threading) as p:
		p.map(main, elements)