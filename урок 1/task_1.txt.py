f = open('test.txt', 'r')
s = f.read()
f.close()
print(s)
s = s.replace('_', ' ')
print(s)
a = s.split()
print(a)
summ = 0
for i in a:
    if i.isdigit():
        summ +=int(i)
print(summ)



