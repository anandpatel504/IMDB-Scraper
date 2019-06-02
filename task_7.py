from task_4 import scrape_movie_details
from task_1 import top_movies
import requests
from bs4 import BeautifulSoup
import pprint
data = top_movies
# print(data)



def analyse_movies_directors():
	
	a=get_movies_list_details(top_movies)

	list_1=[]
	list_2=[]
	for i in a:
		b=(i["director"])
		for i in b:
			list_1.append(i)
	# print(list_1)
			if i not in list_2:
				list_2.append(i)
	# print(list_2)  
	# all_directors=list_2
	# # print(all_directors)
	Dict={}
	for i in list_2:
		counter=0
		for j in list_1:
			if i==j:
				counter+=1
		Dict[i]=counter
	return(Dict)
	pprint.pprint(Dict)

# pprint.pprint(analyse_movies_directors())
