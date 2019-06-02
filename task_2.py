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

# pprint.pprint(group_by_year(data))

# task_3

def group_by_decade(movies):
	list_1 = []
	list_2 = []
	for i in range(1950,2019,10):
		list_1.append(i)
		list_2.append(i+9)
	# print(list_1,list_2)

	dict_1 = {}
	for i in range(len(list_1)):
		first = list_1[i]
		second = list_2[i]
		list_same_year = []
		for j in movies:
			y=j['year']
			if first <= y and second >= y:
				list_same_year.append(j)
		dict_1[first]=list_same_year
	pprint.pprint(dict_1)
	
	
group_by_decade(data)

		


