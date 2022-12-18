# for i in range(10): # range(10) - 0 1 2 3 4 5 6 7 8 9
#     print('Hello!')

# for i in range(10):
#     print(i)
#     if i == 5:
#         print('i = 5 !!!!')

# for i in range(5, 10): # range (5, 10) - 5 6 7 8 9 не включая 10
#     print(i)
# for i in range(1, 20, 2): # range (a, b, c, ) диапозон с шагом c
#         print(i)

# for i in range(20, 1, -2): # в обратную дипозон с шагом c
#     print(i)
# в строку бдует писать от 5 до 10 не включая
# for i in range(5, 10):
#     print(i, end=' ')
#
# print()
# print("Я не отношусь к циклу for")

# for i in 'Я учу Phyton':
#     print(i)

# a = 'я учу PHYTON'
# a_new = ""
# for i in a:
#    #print(i)
#     if i.isupper():
#        # print(i, end=" ")
#        print(a_new)
#        a_new = a_new + i  # a_new +=i
#
# print(a_new)


# a = input("ВВедите строку: ")
# b = input("Введите символ: ")
#
# for i in a:
      # print(i)
#     if i != b:
#         print(i, end="")


#Вводится начало, конец и шаг последовательности, нужно вывести на экран данную последовательность чисел.

# a = int(input("ВВедите начало: ")
# b = int(input("Введите символ: ")
# c = int(input("Введите шаг: ")

#for i in range(54, 101)


# for i in range(55, 9184, 5):
#     print(i)
# for i in range(55, 100):
#      print(i)

#                                 МАССИВЫ

# a = []  # пустой список
# b = [12, 3, 456, 678, 6578, 897]
# s = ['hello', 'world', 'array' ]
#
# for i in s:
#     print(i)
#
# print(len(b))
# print(len(s))

# b = [12, 3, 456, 768, 234, 123, 654]
# for i in b:
#     print(i)
#     if i ==768:
#         break
# print("я не отношусь к циклу for")

# b = [12, 3, 456, 768, 234, 123, 654]
# for i in b:
#     print(i)
#     if i ==768:
#         continue
# print("я не отношусь к циклу for")

# a = [2, 3, 6, 5, 1, 22, 4]
# b = []
# for i in a:
#     if i % 2 == 0:
#         print(i)
#         b.append(i)
# print(b)
# b.append(1234)
# print(b)

# a =[2,5,6,2,2]
# print(a.count(2))

# a = [2,8,10,12]
# b = 0
# p = 1
# for i in a:
#     print(p)
#     b +=i
# print(b)

# a = input("ВВедите строку: ")
# b = input("Введите символ: ")
# a_new = " "
# for i in a:
#
#     if i != b:
#         print(a_new)
#         a_new = a_new + i
#         # print(i, end="")
# print(a_new)
