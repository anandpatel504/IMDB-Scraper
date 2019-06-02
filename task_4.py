from task_1 import top_movies
import requests
from bs4 import BeautifulSoup
import pprint
# print(data)
# movies=top_movies



url = "https://www.imdb.com/title/tt0066763/"
def scrape_movie_details(movie_url):

	Total_detail_list = []

	page = requests.get(movie_url)
		
	soup = BeautifulSoup(page.text,"html.parser")
	# print(soup)

	# title_div = soup.find('div',class_="title_wrapper").get_text().split()
	# movies_name = (title_div[0])

	title_div = soup.find('div',class_="titleBar").h1.get_text()
	a=len(title_div)-8
	movies_name=(title_div[0:a])

	director = soup.find('div',class_="credit_summary_item")
	# print(director)
	director_1 = director.find_all("a")
	director_list = []
	for i in director_1:
		director_list.append(i.text)
	# print(director_list)

	sub_div = soup.find('div',class_="subtext")
	run_time = sub_div.find("time").get_text().strip().split()
	# print(run_time)
	a = len(run_time)
	if a == 1:
		b = run_time[0].split("h")
		# print(b)
		run_time_3 = int(b[0])*60
	else:
		run_time_1 = run_time[0].split("h")
		run_time_2 = run_time[1].split("min") 
		run_time_3 = int(run_time_1[0])*60+int(run_time_2[0]) 
		# print(run_time_3)

	

	poster_image_url = soup.find('div',class_="poster").a['href']
	# print(poster_image_url)
	poster_image_url_1 = "www.imdb.com" + poster_image_url
	# print(poster_image_url_1)


	bio = soup.find('div',class_="plot_summary")
	bio_1 = bio.find('div',class_="summary_text").get_text().strip()
	# print(bio_1)

	country5 = soup.find('div',attrs={"class":"article","id":"titleDetails"})
	country6 = country5.find_all('div',class_="txt-block")

	
	for i in country6:
		h4 = i.find("h4").text
		# print(h4)
		if h4 == "Country:":
			country7 = i.find_all("a")
			for j in country7:
				country8=j.text
			break

	language = soup.find('div',attrs={"class":"article","id":"titleDetails"})
	language_1 = language.find_all('div',class_="txt-block")

	language_list = []
	for i in language_1:
		h4 = i.find("h4").get_text()
		# print(h4)
		if h4 == "Language:":
			language_2 = i.find_all("a")
			for j in language_2:
				language_list.append(j.text)
			# print(language_list)
			break

	genre = soup.find('div',attrs={"class":"article","id":"titleStoryLine"})
	# print(genre) 
	genre_1 = genre.find_all('div',class_="see-more inline canwrap")

	genre_list = []
	for i in genre_1:
		h4 = i.find("h4").text
		# print(h4)
		if h4 == "Genres:":
			genre_2 = i.find_all("a")
			for j in genre_2:
				genre_list.append(j.text)
			# print(genre_list)
		
	Dict = {"movies_name":movies_name,"director":director_list,"Country":country8,"language":language_list,"image_url":poster_image_url_1,"bio":bio_1,"runtime":run_time_3,"genre":genre_list}
	# Total_detail_list.append(Dict)
	return(Dict)
	# pprint.pprint(Total_detail_list)

		# print(movies_name)
		# print(director_list)
		# print(country8)
		# print(language_list)
		# print(poster_image_url_1)
		# print(bio_1)
		# print(run_time_3)
		# print(genre_list)
scrape_movie_details(url)	
# pprint.pprint(scrape_movie_details(url))


