import json
from pprint import pprint
def analyse_language_and_directors():
	# a=get_movies_list_details(top_movies)
	with open("all_movies_details.json","r")as json_file:
		total_movies_data=json.load(json_file)
		# print(total_movies_data)

	list_1=[]
	for i in total_movies_data:
		a=(i["director"])
		for j in a:
			if j not in list_1:
				list_1.append(j)
	# print(list_1)
	director_dict={}
	for k in list_1:
		list_2=[]
		list_3=[]

		for l in total_movies_data:
			b=(l["director"])
			for m in b:
				if m==k:
					language_1=(l["language"])
					# print(language_1)
					for n in language_1:
						list_2.append(n)
						if n not in list_3:
							list_3.append(n)
		dict_language={}
		for p in list_3:
			counter=0
			for q in list_2:
				if q==p:
					counter=counter+1
				dict_language[p]=counter
		director_dict[k]=dict_language
	# return(director_dict)
	pprint(director_dict)

pprint(analyse_language_and_directors())



