# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list_ = [15, 48, 'hello', 6, 19, 'world']
b = []
for i in list_:
    # print(i)
    if type(i) is int:
        # print(i)
        b.append(i)
print(b)
for i in b:
    if i % 2 == 0:
        a = i // 10
        print(a)
        b = i % 10
        print(b)
        c = a + b
        print('Сумма = ', c)
    if i % 2 != 0:
        print('Нечетное = ', i)
        ind = list_.index(i)
        list_[ind] = 1

# list_ = [15, 48, 'hello', 6, 19, 'world']
#
# list_[0] = 1
# print(list_)
# list_[4] = 1
print(list_)
#
list_ = [15, 48, 'hello', 6, 19, 'world']
b = []
for i in list_:
    # print(i)
    if type(i) is str:
        print(i)
        b.append(i)
print(b)
b = "".join(b)
gl = 0
sogl = 0
for i in b:
    if i in 'aeiouy':
        gl += 1
    else:
        sogl +=1
print('Гласные', gl)
print("Согласные", sogl)
