import requests
from bs4 import BeautifulSoup
import sys
import csv
import os
import datetime
import json


def getlink(s, date):
    data = {
        'title_type': 'feature',
        'release_date': date,
        'count': 250
    }

	#Get element
    # https://www.imdb.com/search/title/?title_type=feature&release_date=2022-06-01&count=250
    # lister-item.mode-advanced

    response = s.post('https://www.imdb.com/search/title/?', data=data)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup)

    # <div class="lister-item-content">
    # formalist = soup.select('h3.lister-item-header a')
    formalist = soup.select('div.lister-item-content')
    mvlist = []
    for mv in formalist:
        header = mv.select_one('h3.lister-item-header a').getText()
        link = mv.select_one('h3.lister-item-header a').get("href")
        #storyline = mv.select_one('text-muted p')
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

        mvlist.append({'header': header, 'link': link, 'runtime': runtime, 'type': mvtype})
    print(mvlist)

# Get movie data in detail page and merge data
    mvlist_overall = []
    for mv in mvlist:
        mvinfo = {}
        mvdetail = s.post('https://www.imdb.com' + mv['link'])
        res = mvdetail.text
        mvsoup = BeautifulSoup(res, "html.parser")
        actorlist = mvsoup.select('a.sc-36c36dd0-1')
        characterlist = mvsoup.select('span.sc-36c36dd0-4')
        storyline = mvsoup.select('div.ipc-html-content ipc-html-content--base')
        print(storyline)
        actors = []
        characters = []
        for name in actorlist:
            actor = name.getText()
            actors.append(actor)
        for name2 in characterlist:
            character = name2.getText()
            characters.append(character)
        mvinfo['title'] = mv['header']
        mvinfo['id'] = mv['link']
        mvinfo['poster'] = mvsoup.select_one('div.ipc-media img').get('src')
        mvinfo['trailer'] = 'https://www.imdb.com' + mvsoup.select_one('div.ipc-slate a').get('href')
        if not mvinfo['trailer'].__contains__('https://www.imdb.com/video'):
            mvinfo['trailer'] = 'Null'
        mvinfo['runtime'] = mv['runtime']
        mvinfo['actors'] = actors
        mvinfo['characters'] = characters
        mvinfo['storyline'] = mvsoup.select_one('span.sc-16ede01-2').getText()
        mvinfo['releaseDate'] = str(date)

        # ...

        #print(mvinfo['characters'])
        print('Yes')
        mvlist_overall.append(mvinfo)


# Output to json

# with open('mvlist.json', 'w') as json_file:
#	json.dump(allpendingform, json_file)
#
# return mvlist_overall


""" # create CSV and sqlite3
def create_db():
    create_csv()
 
    conn = sqlite3.connect('top_1000.db')
    c = conn.cursor()
    c.execute('CREATE TABLE top_1000 (title, year, director, cast, imdb_rating);')
    with open('top_1000.csv', 'r') as csv_file:
        dr = csv.DictReader(csv_file)
        to_db = [(i['title'], i['year'], i['director'], i['cast'], i['imdb_rating']) for i in dr]
    c.executemany('INSERT INTO top_1000 (title, year, director, cast, imdb_rating) VALUES (?, ?, ?, ?, ?);', to_db)
    conn.commit()
    conn.close()

create_db()
"""

#running program by date

s = requests.Session()
start_date = datetime.date(2022, 6, 1)
end_date = datetime.date(2022, 6, 1)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    print('Getting ' + str(start_date) + ' IMDB movie data')
    getlink(s, start_date)
    start_date += delta
