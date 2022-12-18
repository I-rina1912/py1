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

b = ''
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

with open("D_Z_14.txt", "r") as file:
    lst = file.read().split()
    lst_numbers = []
    lst_words = []
    for i in lst:
        if i.isdigit():
            lst_numbers.append(int(i))
        else:
            lst_words.append(i)
    print(sorted(lst_numbers)+sorted(lst_words, key= len))