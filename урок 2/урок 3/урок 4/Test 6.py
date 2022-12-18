#СПИСКИ
# elements = [1, 'a', 2, 'b', 5]
# print (elements)
# elements = list()
# print(elements)

# print(elements[-1])
# print(elements[1:4])
# print(elements[::2])

# import random
# a = [random.randint(100, 999) for i in range (10)]  #генерируем список из 10 случайных чисел (числа дмапозон от 100 до 999
# print(a, len(a))  #длина списка

# a = []
# a.append(1234)
# a.append("djgjdj")
# print(a)
# a.insert(0, 'Hello')
# print(a)
# a.insert(1, 789)
# print(a)

# elements = [1, 'a', 2, 'b', 5, 47]
# elements[2] = 777
# print(elements)
# del elements[2] # удаление 2-го индекса
# del elements[1:5] # диапозон удаляем
# del elements[::2] # вся строка с шагом 2
# print(elements)

# elements = [1, 'a', 2, 'b', 5, 47, "a"]
# elements.remove("a")
# print(elements)

# elements = [1, 'a', 2, 'b', 5, 47, "a"]
# print('a' in elements)
# if 'a' in elements:
#     print('Yes')

# a = [1, 2, 3]
# b = [4, 5, 6]
# # print(a+b)
# # d = a + b
# # print(d)
# a.extend(b)
# print(a)


# elements = [1, 'a', 2, 'b', 5, 47, "a"]
# for i in elements:
#     print(i)

# elements = [1, 'a', 2, 'b', 5, 47, "a"]
# el_len = len(elements)
# i = 0
# while i < el_len:
#     print(elements[i])
#     i +=1

# a = [1, 2, 3]
# b = a # ссылка на объект а
# a.append(123)
# a.append(1234567)
# print(a, b)
# print(id (a), id(b))

# a = [1, 2, 3]
# b = a.copy()
# b.append(1234567)
# print(a, b)
# print(id (a), id(b), id(a)== id(b))

# a = [2, 3, 4]
# x = a.pop(1)
# print(a, x)

# a = [2, 3, 'Hello', 4, 5]
# i = a.index('Hello')
# print(i, a[i])
#
# a = [2, 3, 'Hello', 4, 5]
# a.reverse()
# print(a)

# import random
#
# a = [random.randint(1, 10) for i in range(10)]
# print(a)
# a.sort() # по возрастанию
# print(a)
# a.sort(reverse=True) # по убыванию
# print(a)

# a = [2, 3, 'Hello', [4, 5, 6, 'H'], 4, 5]
# a[3].append(346777)
# print(a[3], a[3][-2])


# a = [2, 5, 6]
# print(a[::-1])

# a = [20, 40, 30, 100, 5, 47, 70]
# i = a.index(20)
# if 20 in a:
#     a.index(20)
#     a [i] = 200
# print(a)
#


# a = [20, 40, 30, 'a', 100, 5, 47, 70]
# a.reverse()
# print(a)