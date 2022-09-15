cook_book ={}
with open ('files.txt', 'r', encoding='utf-8') as recepts:
	for line in recepts:
		dish = line.strip()
		count_ingridients = recepts.readline()
		my_list = []
		for i in range(int(count_ingridients)):
			ingridients = recepts.readline()
			ingredient_name, quantity, measure = ingridients.split(' | ')
			all_ingridients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
			my_list.append(all_ingridients)
			cook_book[dish] = my_list
		recepts.readline()

print(cook_book)
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# 	