import requests
import json
from task_1 import top_movies
from bs4 import BeautifulSoup
from pprint import pprint

# url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"


def scrape_movie_cast():

	data=top_movies

	big_list=[]
	for x in data:
		url=(x["url"][0:37]+"fullcredits?ref_=tt_cl_sm#cast")
		page=requests.get(url)
		data=page.text
		soup=BeautifulSoup(page.text,"html.parser")


		div=soup.find('div',class_="article listo")
		# print(div.text)
		table=soup.find('table',class_="cast_list")
		# print(table)

		trs=table.find_all('td',class_='')
		# print(trs)
		# Dict={}
		main_list=[]
		for tr in trs:
			name=(tr.text.strip())
			# print(name)
			# print(name)
			link=(tr.find('a').get('href'))
			# print(link.text)
			# print(link)
			imdb_id=(link[6:15])
			# print(imdb_id)
			Dict={'name':name,"imdb_id":imdb_id}
			# Dict["imdb_id"]=imdb_id
			# Dict["name"]=name
			main_list.append(Dict)
		# pprint(main_list)
		big_list.append(main_list)
	# pprint(big_list)
	return(big_list)

		
# pprint(scrape_movie_cast())
