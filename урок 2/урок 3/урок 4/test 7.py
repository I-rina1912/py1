# my_string = "Apples,Oranges,Pears,Bananas,Berries"
# a = my_string.split(',')
# print(a) # ["Apples, Oranges, Pears,Bananas,Berries"]
#
# my_string = "Apples,Oranges,Pears,Bananas,Berries"
# a = my_string.split(',', 2)
# print(a) # [Apples,Oranges, "Pears,Bananas,Berries"]

# my_arr = ['Apples, Oranges, Pears, Bananas, Berries']
# a = ','.join(my_arr)
# print(a) # Apples, Oranges, Pears, Bananas, Berries

# print('привет' if 5==5 else 'пока')
# print('100 200 300 400'.count('0'))
# print('100 200 300 400'.count('0', 3,7))
# print('100 200 300 400'.count('0'))

# print('100 200 300 400'.count('0'))
# print('100 200 300 400'.count('0', 3, 7))
# print('100 200 300 400'.count('0', 3))

#С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# a = input ('Введите слово: ')
# gl = 0
#sogl = 0
#
# for i in a:
#     if i in 'aeiou':
#         gl += 1
#     else:
#         sogl +=1
# print('Гласные', gl)
# print("Согласные", sogl)

# ВВедсти 3 числа и какео из них среднее
# print('Введите 3 числа: ')
# a = int(input())
# b = int(input())
# c = int(input())
# if b < a < c or c < a < b:
#     print('Среднее', a)
# elif a < b < c or c < b < a:
#     print('Среднее', b)
# else:
#     print('Среднее', c)
# a = int(input('Введите число: '))
# a.reverse()
# print(a)


#Ввести число и перевернуть его
# a = int(input('Введите число: '))
# b = str(a)
# b = b[::-1]
# b = int(b)
# print(b)

# a = [1, 2, 3, 4, 5, 6, 7]
# ch = 0
# n_ch = 0
# s = 0
# for i in a:
#     s += 1
#     if i % 2 == 0:
#         ch += 1
#     else:
#         n_ch += 1
# print('Четные', ch, 'Нечетные', n_ch)
# if ch > n_ch:
#     print('Сумма', s)
# else:
#     print('произведение 1 3 6 элемнтов', a[0]*a[2]*a[5])

# a = 1234567
# ch = 0
# n_ch = 0
# s = 0
# for i in str(a):
#     i = int (i)
#     s += 1
#     if i % 2 == 0:
#          ch += 1
#     else:
#          n_ch += 1
# print('Четные', ch, 'Нечетные', n_ch)
# if ch > n_ch:
#      print('Сумма', s)
# else:
#     print('произведение 1 3 6 элемнтов', a[0]*a[2]*a[5])


#
#
# # Введите слово c клавиатуры, которое состоит из букв разных регистров.
# # Нужно посчитать кол-во пар верхнего регистра. Парой считаются две рядом стоящие буквы верхнего регистра.
# # Например, HeLAQEoO – одна пара LA.
#
# a = input('Введите слово: ')
# up = ''
# p_h = 0
# for i in a:
#     if i.isupper():
#         up += i
#         if len(up) % 2 == 0:
#             p_h += 1
#         print(up)
#     elif up != '':
#         up = ''
# # print(up)
# print(p_h)

# a = input('Введите слово: ')
# a = a.split()
# print(a)
# a = ''.join(a)
# print(a)
# if a == a[::-1]:
#     print('Палиндром')
# else:
#     print("Неполиндром")

# import random
# a = random.randint(1000, 9999)
# print(a)
# for i in a:
#     if i in range (10):
#       print(i.count('1'))

# import random
# r = [random.randint(1000, 9999) for i in range(10)]
# print(r)
# r_s = str(r)
# print(r_s.count('1'))


# s = "привет"
# print(s.islower())

# list_ = [15,48,'hello',6,19,'world']
# a = list_
# b = []
# ch = 0
# n_ch = 0
#
# for i in list_:
#     if type(i) is str:
#         list_.remove(i)
#         print(a)
#
# for i in a:
#     if i % 2 == 0:
#         ch += i
#         print(i)
# list_ = [15, 48, 'hello', 6, 19, 'world']
#
# for x, i in enumerate(list_):
#     if isinstance(i, int):
#         if i % 2 == 0:
#             a = i // 10
#             b = i % 10
#             c = a + b
#             print(f'Сумма =', c)
#         else:
#             list_[x] = 1
# print(list_)
# print(len(list_))



#
# print(i)
# # # i = 0
# ch = 0
# for i in list:
#     if i % 2 == 0:
#         ch += 1
#     print(i)

# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

# list_ = [15, 48, 'hello', 6, 19, 'world']
# b = []
# for i in list_:
#     # print(i)
#     if type(i) is int:
#         # print(i)
#         b.append(i)
# print(b)
# for i in b:
#     if i % 2 == 0:
#         a = i // 10
#         print(a)
#         b = i % 10
#         print(b)
#         c = a + b
#         print('Сумма = ', c)
#     if i % 2 != 0:
#         print('Нечетное = ', i)
#
# list_ = [15, 48, 'hello', 6, 19, 'world']
# list_[0] = 1
# print(list_)
# list_[4] = 1
# print(list_)
# #
# list_ = [15, 48, 'hello', 6, 19, 'world']
# b = []
# for i in list_:
#     # print(i)
#     if type(i) is str:
#         print(i)
#         b.append(i)
# print(b)
# b = "".join(b)
# gl = 0
# sogl = 0
# for i in b:
#     if i in 'aeiouy':
#         gl += 1
#     else:
#         sogl +=1
# print('Гласные', gl)
# print("Согласные", sogl)
#

