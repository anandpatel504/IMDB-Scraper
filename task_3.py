from task_1 import top_movies
import pprint
data = top_movies


def group_by_decade(movies):
	list_1 = []
	list_2 = []
	for i in range(1950,2019,10):
		list_1.append(i)
		list_2.append(i+9)
	# print(list_1,list_2)

	by_decade = {}
	for i in range(len(list_1)):
		first = list_1[i]
		second = list_2[i]
		list_same_year = []
		for j in movies:
			y=j['year']
			if first <= y and second >= y:
				list_same_year.append(j)
		by_decade[first]=list_same_year
	pprint.pprint(dict_1)
	
	
group_by_decade(data)

		
