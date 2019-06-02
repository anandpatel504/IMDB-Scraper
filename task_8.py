from task_4 import scrape_movie_details
from task_1 import top_movies
import requests
from bs4 import BeautifulSoup
import pprint
data = top_movies
# print(data)

import json
def movies_json():
	# pprint.pprint(l)

	n=top_movies
	for i in n:
		o=i["url"]
		# print(o)
		l=scrape_movie_details(o)

		movies_link=(i["url"][27:36])
		m=movies_link+".json"
		with open(m,"w+")as json_file:
			json.dump(l,json_file)  
	
movies_json()