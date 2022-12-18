#КОРТЕЖ  те же списки, неизменяемый тип данных
# a = (1, 2, 3, 4, 5, 6)
# b = (1,)
# print(a, b)
#
# a1 = 1, 2, 3, 4, 5, 6
# print(a1, type(a1))
#
# a2 = tuple()  #пустой кортеж
# print(a2, type(a2))
#
# a3 = ()
# print(a3, type(a3))
#
# a = (1, 2, 3, 4, 5, 6) #меньше весит
# b = [1, 2, 3, 4, 5, 6]
# print(a. __sizeof__())
# print(b.__sizeof__())

# Имеет К. ИНДЕКСЫ, срезы, и -1 обрат
# a = (1, 2, 3, 4, 5, 6)
# print(a[0:3])
# print(a[:3])
# print(a[1:])
# print(a[2::2])
# print(a[::2])

# a = (1, 3, 'hi!', 123, 4)
# b = list(a)
# print(b)
# b.append('hello')
# print(b)
# b_c = tuple(b)
# print(b_c)

# nested = (1, 'do', ['param', 10, 20])
# nested[2][1] = 15
# print(nested)
# print(nested[2][0])


# x = (1, 2, 3, 4)
# y = (5, 6, 7, 8)
#
# print(x + y)
#
# z = x + y
# print(z)


# x = (1, 2, 3, 4)
# print(x*2)
# z = x * 2  # к спискам тоже можно применять
# print(z)

# x = (1, 2, 2, 3, 4)
# print(x.count(2), len(x))   # counte сколько раз посторяется    len длинна
# print(x.index(4))

# x = (1, 2, 2, 3, 4)
# print('max:', max(x), 'min:', min(x))  # к спискам тоже можно применять

# x = ('phyton', 'java', 'c')
# print('max:', max(x, key=len),  'min:', min(x, key=len))  #к спискам тоже можно применять

# a = 'asd'
# print(max(a), min(a))

# x = (1, 2, 2, 3, 4)
# print(sum(x))   # к спискам тоже можно применять


# a = (1, 3, 'hi!', 123, 4)
# if 'hi!' in a:
#     print('hi')

# a = (1, 3, 'hi!', 123, 4)
# for i in a:
#     print(i)

# ЗАДАЧА 1
# Создайте Кортеж из случайных 10 чисел. Найдите его максимальный  и иминимальный элемент.
# import random
# a = [random.randint(0, 100) for i in range(10)]
# a = tuple(a)
# print(a)
# print('max', max(a), 'min', min(a))

#ЗАДАЧА 2
# import random
# a = [random.randint(0, 5) for i in range(10)]
# print(a)
# b = tuple(a)
# print(b)
# print('max:', max(b), 'min:', min(b))

#ЗАДАЧА 3
# Заполните один кортеж десятью случайными целыми
# числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа, создав тем самым третий кортеж.
# Выведите на экран третий кортеж и количество нулей в нем.
# import random
# a = tuple([random.randint(0, 5) for i in range(10)])
# b = tuple([random.randint(-5, 0) for i in range(10)])
# c = a + b
# print(c)
# print('Количество нулей: ', c.count(0))


#ЗАДАЧА 4
# Ввести данные кортежа без скобок, через запятую
# a = ('ty', 'pop', 'you', 'hi')  # если все строки
# b = ','.join(a)
# print(b)

# a = (1, 3, 'hi!', 123, 4)          # если в перемешку и строки и числа
# x = ','.join([str(i) for i in a])
# print(x)

# print('\tHello, World!')
# print("\U0001f601")
