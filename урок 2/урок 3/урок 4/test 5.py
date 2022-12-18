# while True:
#     print("Hello") #бесконечн

# i = 0
# while i < 10:  # 10-конец
#     print(i)
#     if i == 5:
#         break
#     i = i + 1 # i +=1 шаг

# i = 0
# r = 0
# while i < 51:
#     r += i
#     # print(i)
#     i += 1
# print('Сумма  , r')

# i = 0
# while i < 10:
#     i += 1
#     print (i ** 2)

# i = 1
# p = 1
# while i < 125:
#     i += 1
#     if i % 2 == 0:
#        p *= i
#        print(p)

# i = 0
# while i < 10:  # 10-конец
#     print(i)
#     # if i == 5:
#     #  break
#     i = i + 1 # i +=1 шаг
# else:
#     print("Готово!")

# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print("Готово!")


# i = 16
# while i > 0:
#     i = i - 1
#     print(i)
#     if i == 16:
#       break

# i = 0
# r = 7
# while i < 98:
#        i += 7
#        r += i
#        print(i)

# i = 0
# r = []
# while i < 98:
#     i += 7
#     print(i)
#     r.append(i)
# i += 1
# print(r)
# print(len(r))

# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# while True:
#     a = float(input('a = '))
#     b = float(input('b = '))
#     s = input('Введите + - * / или 0 - для выхода: ')
#     if s == '0':
#         break
#     elif s == '+':
#         print(a + b)
#     elif s == '-':
#         print(a - b)
#     elif s == '*':
#         print(a * b)
#     elif s == '/':
#         if b != 0:
#             print(a / b)
#         else:
#             print('Делить на ноль нельзя!')