import requests
from bs4 import BeautifulSoup
import sys
import csv
import datetime
import json


def getlink(s,date):
	
	data = {
		'title_type':'feature',
		'release_date':date,
        'count':250
		}
	
		#https://www.imdb.com/search/title/?title_type=feature&release_date=2022-06-01
        #lister-item.mode-advanced
	
	response = s.post('https://www.imdb.com/search/title/?',data=data, proxies={'http':'','https':''},verify=False)
	html_content = response.text

	soup = BeautifulSoup(html_content, "html.parser")
	#print(soup)
	
	#<div class="lister-item-content">
	#formlist = soup.select('h3.lister-item-header a')
	formlist = soup.select('div.lister-item-content')
	mvlist = []
	for mv in formlist:
		header = mv.select_one('h3.lister-item-header a').getText()
		link = mv.select_one('h3.lister-item-header a').get("href")
		runtime = mv.select_one('span.runtime')
		if runtime != None:
			runtime = runtime.getText()
		else:
			runtime = 'Null'

		mvtype = mv.select_one('span.genre')
		if mvtype != None:
			mvtype = mvtype.getText().strip('\n').strip(' ')
		else:
			mvtype = 'Null'
		
		
		mvlist.append( {'header':header,'link':link, 'runtime':runtime, 'type':mvtype} )
	print(mvlist)
    
    mvlist_overall = []
	for mv in mvlist:
		mvinfo = {}
		mvdetail = s.post('https://www.imdb.com'+mv['link'], proxies={'http':'','https':''},verify=False)
		res = mvdetail.text
		mvsoup = BeautifulSoup(res, "html.parser")
		mvinfo['title'] = mv['header']
		mvinfo['poster'] = mvsoup.select_one('div.ipc-media img').get('src')
		mvinfo['trailar'] = 'https://www.imdb.com'+mvsoup.select_one('div.ipc-slate a').get('href')
		mvinfo['runtime'] = mv['runtime']
        
        #...
        
        
		print(mvinfo['runtime'])
		
        mvlist_overall.append(mvinfo)
        
    
	#with open('eform.json', 'w') as json_file:
	#	json.dump(allpendingform, json_file)
	#	
	#return allpendingform
	

s = requests.Session()
start_date = datetime.date(2022, 6, 1)
end_date = datetime.date(2022, 6, 1)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
	print(start_date)
	getlink(s,start_date)
	start_date += delta