from collections import Counter
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)
print(c['red'])
print(sum(c.values()))
print(c.values())


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

#Сложение
print(counter_moscow + counter_spb)
# Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})

# Вычитание
counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

# Вычитание, при котором нет значений меньше 1
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})

# Чтобы получить список всех элементов, которые содержатся в Counter в алфавитном порядке
print(*counter_moscow.elements())
# black black black black white white yellow yellow yellow

#Чтобы получить список уникальных элементов
print(list(counter_moscow))
# ['black', 'white', 'yellow']

# С помощью функции dict() можно превратить Counter в обычный словарь:
print(dict(counter_moscow))
# {'black': 4, 'white': 2, 'yellow': 3}

# Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print(counter_moscow.most_common())
# [('black', 4), ('yellow', 3), ('white', 2)]

# функция clear() позволяет полностью обнулить счётчик:
counter_moscow.clear()
print(counter_moscow)
# Counter()
