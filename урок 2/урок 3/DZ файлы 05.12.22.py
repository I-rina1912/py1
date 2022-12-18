
# 1 вариант

# f = open('text.txt', 'r', encoding='utf-8')
# a = 0
# for line in f:
#    a += 1
# print('Кол-во строк:', a)
#
# f = open('text.txt', 'r', encoding='utf-8')
# s = f.readlines()
# f.close()
#
# s_new = []
# for i in s:
#     i = i.replace('\n', '')
#     s_new.append(i)
# # print(s_new)
# for i in s_new:
#     print('Кол-во символов в строке:', len(i))

# 2 вариант

# si = sum(1 for line in open('text.txt'))
# print('Кол-во строк:', si)
# with open('text.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.rstrip('\n\r')
#         print(line)
#         print('Кол-во символов в строке', len(line))

