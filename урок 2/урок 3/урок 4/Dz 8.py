# a = input('Введите текст: ')
# b = ''
# arr = []
# for i in a:
#     if i.isalpha():
#         b += i
#     elif b != '':
#         arr.append(b)
#         b = ''
# if b != '':
#     arr.append(b)
# print(' '.join(arr))
#
# print('max:', max(arr, key=len))
#
# text = input("Введите текст: ")
# alpha = []
# for i in text:  # перебираем каждый элемент
#     if i.isalpha() or i == " ":  # создаем новый список без знаков.
#         alpha.append(i)
# cort = tuple("".join(alpha).split())  # преобразовал в строку, после в список и в кортеж
# print(cort, '\n'  "Самое длинное слово: ", max(cort, key=len))