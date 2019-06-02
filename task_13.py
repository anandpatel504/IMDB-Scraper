import requests
import json
from task_12 import scrape_movie_cast
from bs4 import BeautifulSoup
from pprint import pprint



def scrape_movie_cast_with_all_detail():

	data=scrape_movie_cast()
	# pprint(data)
	
	with open("all_movies_details.json","r")as json_file:
		total_movies_data=json.load(json_file)
		# print(total_movies_data)

	for i in range(len(total_movies_data)):
		Dict={}
		b=(total_movies_data[i])
		# print(b)

		list_1=[]
		for j in b:
			list_2=[]
			# print(j)
			list_1.append(j)
		# pprint(list_1)
		Dict_1={}
		for key in list_1:
			main_value=(b[key])
			Dict_1[key]=main_value
		# pprint(Dict_1)
		Dict_1["cast"]=data
		pprint(Dict_1)
			


scrape_movie_cast_with_all_detail()
