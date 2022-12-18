# try:
#     a = 100 / 0
# except ZeroDivisionError:
#     print('произошло деление на ноль')
#     a = 0
# print('результат:', a)


# try:
#     a = 100 / '0'
# except Exception as e:
#     print(e)
#     a = 0
# print('результат:', a)


#СЛОВАРИ
# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['v']
# except KeyError:
#     print('Ключа не сущ-ет!')

#СПИСКИ
# l = [1, 2, 3, 4, 5]
#
# try:
#      a = l()
# except IndexError:
#     print('Такого индекса не сущ-ет!')
# except KeyError:
#      print('Ключа не сущ-ет!')
# except:
#     print('Произошла другая ошибка')


# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['v']
# except (KeyError, IndexError):
#     print('Произошла ошибка IndexError или KeyError')
# # finally:
# #     print('Оператор finally выполнен')
# else:                            # выполниться, если ошибок нету
#     print('Ошибок не произошло')
#


# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['a']
# except (KeyError, IndexError):
#     print('Произошла ошибка IndexError или KeyError')
# else:
#     print('Ошибок не произошло')
# finally:
#     print('Оператор finally выполнен')


# Введите два числа с клавиатуры.
# Поделите одно на другое.
# Обработайте ошибку деления на ноль, если ошибок нет, то результат
# деления возвести
# в квадрат. Также используйте оператор finally.

# a = int(input('Введите число:'))
# b = int(input('Введите число:'))
#
#
# try:
#     s = a / b
#     print(s)
# except ZeroDivisionError:
#     print('произошло деление на ноль')
#     s = 0
# else:
#      print('Ошибок не произошло')
#      p = s ** 2
#      print('Деление в 2-ую степень', p)
# finally:
#     print('Оператор finally выполнен')

