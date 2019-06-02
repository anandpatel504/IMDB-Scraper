import json 
from pprint import pprint

def analyse_movies_genre():
	with open("all_movies_details.json","r")as json_file:
		total_movies_data=json.load(json_file)
		# print(total_movies_data)

	list_1=[]
	list_2=[]
	# main_genre_dict={}
	for i in total_movies_data:
		a=(i["genre"])
		for j in a:
			list_1.append(j)
	# print(list_1)
			for k in list_1:
				if k not in list_2:
					list_2.append(k)

	genre_dict={}
	for l in list_2:
		counter=0
		for m in list_1:
			if l==m:
				counter=counter+1
			genre_dict[l]=counter
	pprint(genre_dict)
	# pprint(main_genre_dict)
		


analyse_movies_genre()