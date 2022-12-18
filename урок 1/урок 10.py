# МНОЖЕСТВО

# a = {12, 42, 124, 5, 5, 5, 8, 9832}
# print(a, type(a))
#
# b = set()
# print(b, type(b))
#
# a_2 = {'Python', 'Java', 'JS'}
# print(a_2)
# a_3 = {1, 6, 7, 'JS', 2, 6, (1, 2, 3)}  # элементы М. - неизмю тип даннных
# print(a_3)


# a = [2, 3, 4, 5, 'py', 'py', 1, 22, 3, 3, ]
# x = set(a)
# a_1 = list(x)
# print(set(a), x)
# print(a_1)

# month = {'Jan', 'Feb', 'March'}
# print("March" in month)
# for m in month:
#     print(m, end=', ')
# # print("May" in months)
#
# month.add('Feb')
# print(month)

# num_set = {1, 2, 3, 4, 5, 6}
# num_set.discard(3)    #УДАЛЕНИЕ
# print(num_set)
#
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.remove(3)   # удаление, но программа остановится
# print(num_set)


# num_set = {1, 2, 3, 4, 5, 6}
# num_set.pop()
# print(num_set)

# num_set = {1, 2, 3, 4, 5, 6}
# num_set.clear()
# print(num_set)

# month_a = {'Jan', 'Feb', 'March'}
# month_b = {'July', 'Aug'}
# m = {1, 2}
# all_month = month_a.union(month_b, m)
# print(all_month)


# x = {1, 2, 3}   #ОБЪЕДИНЕНИЕ
# y = {4, 5, 6}
# z = {7, 4, 9}
# output = x.union(y, z)
# output_2 = x | y | z
# print(output)
# print(output_2)

# ПЕРЕСЕЧЕНИЕ
# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9, 3}
# print(x & y & z)

# РАЗНИЦА МЕЖДУ М.
# A = {1, 2, 3}
# B = {4, 3, 6}
# print(A - B)
# print(B - A)


# names_a = {'Nicholas', 'John', 'Mercy'}
# names_b = {'Jeff', 'Bosco'}
# x = names_a.isdisjoint(names_b)
# print(x)
# print(len(names_a))

# my_set = frozenset([1, 2, 3, -10, 40])
# print(type(my_set))

# a = [2, 4, 5, 2, 8]
# x = set(a)
# print(a)
# print(x)
# print(len(a))
# print(len(x))
# if len(a) > len(x):
#         print('Есть дубликаты')
#
#         lst = [0, 1, 1, 2, 3]
#         set_1 = set(lst)
#         if len(lst) == len(set_1):
#             print("нет")
#         else:
#             print("да")


# a = {1, 2, 5, 7, 8}
# b = frozenset([1, 2, 3, -10, 40])
# s = a | b
# print('Объединение', s)
# print('Пересечение', a & b )



# a = 'python, JS! C?'
# for i in a:
#     if not i.isalpha() and i != ' ':
#         a = a.replace(i, '')
# b = a.split()
# print(b)
# b = set(b)
# print(b)