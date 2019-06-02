import pprint
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
page = requests.get(url)
# print(page)
data = page.text
# print(data)	

soup = BeautifulSoup(page.text,"html.parser")

title = soup.title
# print(title)

def scrape_top_list():
	main_div = soup.find('div',class_='lister')
	tbody = soup.find('tbody',class_='lister-list')
	trs = tbody.find_all('tr')

	position_of_movie = []
	name_of_movie = []
	year_of_movie = []
	rating_of_movie = []
	url_of_movie = []

	rank = 0
	Dict={}
	list1=[]
	for tr in trs:
		

		position = tr.find('td',class_="titleColumn").get_text().strip().split()

		name = tr.find('td',class_="titleColumn")
		name_1 = name.a.get_text()
		# name_of_movie.append(name)
		
		year = name.find('span').get_text()
		# year_of_movie.append(year)
		
		movies_rating = tr.find('td',class_="ratingColumn imdbRating").get_text().split()
		# rating_of_movie.append(movies_rating)

		url_link = tr.find("a").get("href")
		url_link_1 = ("https://www.imdb.com" + url_link)
		# url_of_movie.append("www.imdb.com" + url_link)
		# print(url_link_1)
		

		Dict = {'position':int(position[0].strip('.')),'name':position[1],'year':int(year[1:5]),'rating':float(movies_rating[0]),'url':url_link_1}
		list1.append(Dict)
		# print(list1)
	return list1
		
top_movies = scrape_top_list()
# pprint.pprint(top_movies)
