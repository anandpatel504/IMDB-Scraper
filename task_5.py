from task_4 import scrape_movie_details
from task_1 import top_movies
import requests
from bs4 import BeautifulSoup
import pprint
data = top_movies
# print(data)

	
def get_movies_list_details(movies_link):
# top_movies = scrape_movie_details("https://www.imdb.com/title/tt0066763/")
	top_movies_list = []
	for i in range(len(data)):
		if i==10:
			break
		else:
			a=(data[i]['url'])
			top_movies=scrape_movie_details(a)
			# pprint.pprint(top_movies)
		top_movies_list.append(top_movies)
	return(top_movies_list)
	# pprint.pprint(top_movies_list)


# get_movies_list_details(top_movies) 
pprint.pprint(get_movies_list_details(top_movies))

