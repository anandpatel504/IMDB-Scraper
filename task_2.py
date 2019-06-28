from task_1 import top_movies
import pprint
data=top_movies


def group_by_year(movies):
	# print(movies)
	list_of_year = []
	for i in movies:
		a = i["year"]
		if a not in list_of_year:
			list_of_year.append(a)
	# print(list_of_year)
	dict_1={}
	for i in list_of_year:
		list_1=[]
		for j in movies:
			bar=j["year"]
			if bar == i:
				list_1.append(j)
		dict_1[i]=list_1
	return (dict_1)

pprint.pprint(group_by_year(data))


	


		


