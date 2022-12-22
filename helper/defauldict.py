#Defaultdict позволяет задавать тот тип данных, который хранится в словаре по умолчанию
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
#Создадим defaultdict, в котором при обращении по несуществующему ключу будет автоматически создаваться новый список
#Для этого при создании объекта defaultdict в круглых скобках передадим параметр list:
from collections import defaultdict
groups = defaultdict(list)
for student, group in students:
    groups[group].append(student)
 
print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})
#Получить элемент из defaultdict по ключу можно так же, как и из обычного словаря:
print(groups[3])
# ['Petrov', 'Markov']
