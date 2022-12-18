# #  Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# # (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
# # а также сколько всего букв в слове, сколько гласных и согласных.
#
# a = input('Введите слово: ')
# up = ''
# up_1 = ''
# up_2 = 0
# p_h = 0
# for i in a:
#     if i.isupper():
#         up += i
#         if len(up) % 2 == 0:
#             p_h += 1
#         print(up)
#     elif up != '':
#         up = ''
#     if i.islower():
#         up_1 += i
#         if len(up_1) % 2 == 0:
#             up_2 += 1
#         print(up_1)
#     elif up_1!= '':
#         up_1 = ''
# print(up)
# print('Пар гласных', up_2)
# print ('Пар согласных', p_h)
# print(len(a))
# gl = 0
# sogl = 0
# for i in a:
#     if i in 'aeiouy':
#         gl += 1
#     else:
#         sogl +=1
#     if gl == sogl:
#         print(gl)
# print('Гласные', gl)
# print("Согласные", sogl)
# #
# a = 'я сегодня съела 500 ккал углеводов 500 ккал белка 200 ккал жиров'
# b = ''.join(a)
# print(b)
# print(b[16:19])
# print(b[35:38])
# print(b[50:53])

# 4.Посчитать, сколько раз встречается определенная цифра в
# числах. Количество введенных чисел и искомая цифра задаются
# с клавиатуры. Числа выбираются рандомно.

# import random
# b = int(input('Введите кол-во введеных чисел: '))
# r = [random.randint(0, 10000) for i in range(b)]
# print(r)
# isk = int(input('Введите искомую цифру: '))
# c = 0
# for i in r:
#     for k in str(i):
#         if int(k) == isk:
#             c += 1
# print('Цифра', isk, "встречается",c, 'раза' if c == 2 or c == 3 or c == 4 else 'раз' )



# 3. Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры
# окажется больше рандомной пары (первое введённое число больше первого рандомного
# и второе введённое больше второго рандомного). Проверку выполнить 6 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаев)
# вывести случайные числа, полученные в 4 итерации.
# import random
# i = 1
# bol = 0
#
# while i <= 6:
#     print('Проверка №', i)
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     print(r1, r2)
#     a = int(input('a = '))
#     b = int(input('b = '))
#
#     if a > r1 and b > r2:
#         bol += 1
#
#     if i == 4:
#         it_4_1 = r1
#         it_4_2 = r2
#
#     i += 1
#
# if bol == 3:
#     print('Случайные числа ', it_4_1, it_4_2)


# a = int(input('Введите7 значное  число: '))
# if len(str(a)) == 7:
#     ch = 0
#     n_ch = 0
#     s = 0
#     for i in str(a):
#         if int(i) % 2 == 0:
#             ch += 1
#         elif int(i) % 2 == 1:
#             n_ch += 1
#         s += int(i)
#     if ch > n_ch:
#         print(s)
#     elif n_ch > ch:
#         print(int(str(a)[0])*int(str(a)[2])*int(str(a)[5]))
# else:
#     print('error')
#  3 задача
# i = 1
# bol = 0
#
# while i <= 6:
#     print('Проверка №', i)
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     print(r1, r2)
#     a = int(input('a = '))
#     b = int(input('b = '))
#
#     if a > r1 and b > r2:
#         bol += 1
#
#     if i == 4:
#         it_4_1 = r1
#         it_4_2 = r2
#
#     i += 1
#
# if bol == 3:
#     print('Случайные числа ', it_4_1, it_4_2)