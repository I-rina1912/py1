# 1.С клавиатуры вводится 7 значное число. Если четных цифр в нем
# больше, чем нечетных, то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 цифры.

# num = input('Введите семизначное число: ')
# list_num = []
# for i in num:
#     list_num.append(int(i))
# print(list_num)

# ch = 0
# n_ch = 0
# sum_num = 0
#
# for i in list_num:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         n_ch += 1
#
# print('Четные', ch, 'Нечетные', n_ch)
# if ch > n_ch:
#     for i in list_num:
#         sum_num += i
#     print('Сумма', sum_num)
# else:
#     print('произведение 1 3 6 цифр', list_num[0] * list_num[2] * list_num[5])

#2.  С клавиатуры вводится текст, определить, сколько в нём гласных,
# а сколько согласных. В случае равенства вывести на экран все гласные буквы.
# a = input('Введите слово на английском: ')
# gl = 0
# sogl = 0
# gl_1 = ''
# sogl_2 = ''
# for i in a:
#     if i in 'aeiouy':
#         gl += 1
#     else:
#         sogl +=1
# for i in a:
#     if i in 'aeiouy' :
#       gl_1 += i
#     else:
#       sogl_2 += i
#         # print(sogl_2)
# if len(gl_1) == len(sogl_2):
#        print(gl_1)
# print('Гласные', gl)
# print("Согласные", sogl)



#  5.Вводится строка, содержащая буквы, целые неотрицательные
# числа и иные символы.  Требуется все числа, которые
# встречаются в строке отдельно вывести на экран. Строка может содержать пробелы.


# a = 'qwe123*$5 45 h*'
# print(a)
# b = []
# for i in a:
#     if i.isdigit():
#         b.append(int(i))
# print(b)
# a = input('Введите строку: ')
# b = ''
# arr = []
# for i in a:
#     if i.isdigit():
#         b += i
#     elif b != '':
#         arr.append(b)
#         b = ''
# if b != '':
#     arr.append(b)
# print(', '.join(arr))

#6. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
# а также сколько всего букв в слове, сколько гласных и согласных.

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
#              up_2 += 1
#         print(up_1)
#     elif up_1!= '':
#         up_1 = ''
# print(up)
# print('Пар Нижнего регистра', up_2)
# print('Пар Верхнего регистра', p_h)
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

# a = input('Введите слово на английском: ')
# up = ""
# low = ""
# p_u = 0
# p_l = 0
# for i in a:
#     if i.isupper():
#         up += i
#         if len(up) % 2 == 0:
#             p_u += 1
#     elif up !="":
#         up = ""
    #print(up)
# for i in a:
#     if i.islower():
#         low += i
#         if len(low) % 2 == 0:
#             p_l += 1
#     elif low !="":
#         low = ""
#
# gl = 0
# sogl = 0
# for i in a:
#     if i.lower() in 'aeiouy':
#         gl += 1
#
#     else:
#         sogl += 1
#
# print("В нижнем -", p_l, " В верхнем -", p_u, "\n","Всего букв", len(a)  )
# print('Гласные', gl)
# print('Согласные', sogl)

# a = input('Введите строку: ')
# p_up = 0
# p_low = 0
# up = ''
# low = ''
# gl = 0
# sogl = 0
# for i in a:
#     if i.lower() in 'aeoiu':
#         gl += 1
#     else:
#         sogl += 1
#     if i.islower():
#         low += i
#         if len(low) % 2 == 0:
#             p_low += 1
#     elif low != '':
#         low = ''
#
#     if i.isupper():
#         up += i
#         if len(up) % 2 == 0:
#             p_up += 1
#     elif up != '':
#         up = ''
# print('Гласные ', gl, 'Согласные', sogl)
# print('Пары нижнего ', p_low, 'Пары верхнего', p_up)
