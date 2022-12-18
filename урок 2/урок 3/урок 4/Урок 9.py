# СЛОВАРИ

# d = {}
# d = {'dict': 1, 'dictionary': 2}
# print(d)

# a = {'one': 1,
#      2: 'two',
#      (3, 4,): [1, 3, 4, 5]} # неизменяемый тип данных; значения ВСе ТИпы данных
# print(a)

# a = dict()
# a_2 = {}
# print(a, type(a))

# d = dict([(1, 'one'), ('one', [1, 2, 3]), (2, 2)])
# print(d)

# d = dict(one=1, two='hello')  # только если КЛЮЧ СТРОКА
# print(d)

# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)

# import random
#
# d = {i: i**2 for i in range(7)}
# print(d)
#
# d_2 = {i: random.randint(1, 10) for i in range(7)}
# print(d_2)
#
# key = ['a', 'b', 1, (2, 3)]
# d_3 = {i: random.randint(1, 10) for i in key}
# print(d_3)

# a = {'one': 1,
#      2: 'two',
#      (3, 4,): [1, 3, 4, 5]}  # неизменяемый тип данных; значения ВСе ТИпы данных
#
# a[3] = 77  # добавление новой пары
# a[2] = 123  # изменение существующей пары
# print(a)
# print(a['one'])
# print(len(a))

# Salary = {'Director': 120800.0,
#           'Secretary': 101150.25,
#           'Locksmith': 188200.00}
# print(Salary)
# del Salary['Secretary']
# print(Salary)

# Удалить элемент по ключу 'Secretary' с проверкой
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)

# Попытка удалить несуществующий ключ
# если ключа нету, то исключение KeyError не генерируется
# key2 = 5
# if key2 in Salary:
#     del Salary[key2]

# phone = {'pixel': [1, 2, 3, 4],
#          'samsung': ['a1', 'a2', 'a3', 'a4'],
#          'cost': {'pixel_3': 300,
#                   'samsung_a1': 200}
#          }
# print(phone['pixel'][2])
# print(phone['cost']['pixel_3'])

# # 1. Сформировать пустой словарь
# Words = dict() # Words = {}
#
# # 2. Ввести кол-во слов в словаре
# count = int(input('Кол-во слов в словаре: '))
#
# # 3. Цикл добавления слов
# # i = 0
# while i < count:
#     print("Ввод слов")
#     wrd = input('Слово: ')
#     value = int(input('Значение: '))
#
#     # Если ключа wrd нет в словаре, то добавит пару [wrd:value}
#     if wrd not in Words:
#         Words[wrd] = value
#     i = i + 1
# # Вывести сформированный словарь
# print(Words)


# Словари. Функция zip()


# Numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(Numbers)

# months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr'}
# for i in months:
#     print(i, ":", months[i])
#
# print(months.keys())
# print(months.values())
# print(months.items())  # пара в кортеже будет показана
#
# for key, values in months.items():
#     print(key, ':', values)

# person = {'name': 'Irina',
#           'age': 30,
#           'city': 'Minsk'}
# print(person['age'])

# slovar = {'BMW': [1, 2, 3],
#           'Tesla': ['1t', '2d', '3t']
#           }
# print(slovar['BMW'][0], slovar['BMW'][-1])
# print(slovar['Tesla'][0], slovar['Tesla'][-1])
# #
# auto = {"BMW": [1, 2, 3],
#         "Tesla": ["s1", "s2", "s3"]
#         }
# print("1-я и 3-я модели BMW: ", auto["BMW"][0], auto["BMW"][2], "\n",
#       "1-я и 3-я модели Tesla: ", auto["Tesla"][0], auto["Tesla"][2])



# Дан словарь с числовыми значениями. Необходимо
# их все перемножить и вывести на экран.

# a = {'a': 10, 'b': 2, 'c': 5}
# r = 1
# for i in a:
#     r *= a[i]
# print(r)
