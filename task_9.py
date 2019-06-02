import random
import time
import json
def movies_json():
	# pprint.pprint(l)

	n=top_movies
	new_list = []
	for i in n:
		o=i["url"]
		# print(o)
		time_1 = random.randint(1,3)
		time.sleep(time_1)
		l=scrape_movie_details(o)
		new_list.append(l)

		movies_link=(i["url"][27:36])
		m=movies_link+".json"
		with open(m,"w+")as json_file:
			json.dump(l,json_file)
	with open("all_movies_details.json",'w+')as json_data:
		json.dump(new_list,json_data)  
	
