# ФАЙЛЫ

# f = open('test.txt', 'r', encoding='utf-8')
# print(f)
# print(*f)
# f.close()
import os

# f = open('test.txt', 'r', encoding='utf-8')
# try:
#     print(*f)
# finally:
#     f.close()

# with open('test.txt', 'r', encoding='utf-8') as f:
#     print(*f)
#
# print('не отношусь к блоку with')
#
# f = open('test.txt', 'r', encoding='utf-8')
# # print(f.read(7))
# # print(f.read(7)
# # print(f.read())
# s = f.read()
# f.close()
#
# print(s, type(s))

# f = open('test.txt', 'r', encoding='utf-8')
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readlines())
# s = f.readlines()
# f.close()
#
# s_new = []
# for i in s:
#     i = i.replace('\n', '')
#     s_new.append(i)
# print(s_new)

# f = open('123.txt', 'w', encoding='utf-8') #дополнительный режим на запись и чтения
# f.write('Hello \nWorld!')
# f.close()

#  import os
#
#  os.rename('123.txt', 'new_file.txt')
#
# print('Текущая директория: ', os.getcwd())
# os.mkdir('folder')

# import os
#
# print('Текущая директория: ', os.getcwd())
# os.chdir('folder')
# print('Текущая директория: ', os.getcwd())
# f = open('123.txt', 'w', encoding='utf-8')
# f.close()

# import os
#
# print('Текущая директория: ', os.getcwd())
# os.chdir('folder')
# print('Текущая директория: ', os.getcwd())
# os.chdir('..')
# print('Текущая директория: ', os.getcwd())
#
# os.makedirs('n1/n2/n4')

# import os
# # os.remove('folder/123.txt')
# # os.rmdir('folder')
# os.removedirs('n1/n2/n4')


# f = open('test.txt', 'r')
# s = f.read()
# f.close()
# print(s)
# s = s.replace('_', ' ')
# print(s)
# a = s.split()
# print(a)
# summ = 0
# for i in a:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# Файл содержит числа и буквы. Каждый записан в отдельной строке
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию
# а потом слова по возрастанию их длинны
# python
# c
# 2
# 1
# java
# 5
# 3

f = open('test.txt', 'r')
s = f.read()
f.close()

a = s.split()
print(a)
s1 = []
s2 = []

for i in a:
    if i.isdigit():
        s1.append(i)
    if i.isalpha():
        s2.append(i)

print(s1)
print(s2)
s1.sort()
print(s1)
s2.sort(key=len)
print(s2)
s3 = s1 + s2
print(s3)


