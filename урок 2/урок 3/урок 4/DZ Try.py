# Ввд с клавиатуры.
# Если строка введенная с клавиатуры - это числа, то поделить первое и второе.
# Обработать ошибку деления на ноль.
# Если второе число 0, то программа запрашивает ввод чисел заново.
# Также, если былли введены буквы, то обработать исключение.

try:
    a = input('Введите первое значение: ')
    b = input('Введите второе значение: ')
    s = int(a) / int(b)
    print('Деление первого на второе: ', s)
except ZeroDivisionError:
    print('Произошло деление на ноль')
    s = 0
    a = input('Введите первое значение: ')
    b = input('Введите второе значение: ')
    s = int(a) / int(b)
    print('Ошибок не произошло!')
except ValueError:
    print('Введен неправильный тип данных')
finally:
    print('Оператор finally выполнен')


