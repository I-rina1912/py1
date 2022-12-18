# У вас есть словарь, где ключ - название продукта. Значение - список, который
# содержит цену и кол-во товара.
# Вывести через "-" название - цену- количество.
# С клавиатуры вводите название товара и его кол-во.
# n - выход из программы
# посчитать цену выбранных товаров и сколько  осталось в изначальном списке.

m = {'Banan': [2, 100],
     'Apple': [1, 50],
     'Peach': [4, 30],
     'Grape': [5, 70]
     }
for key, values in m.items():
    print(key, '-'.join(str(num) for num in values), sep='-')
# # print('Banan', '-', m['Banan'][0], '-', m['Banan'][1])

i = 0
while True:
    p = input('Введите название продукта: ')
    k = int(input('Кол-во продукта: '))
    if p in m:
        print('Продолжайте покупку')
    else:
        print('Такого не существует!')
        p = input('Введите название продукта: ')
    cost = (m[p][0])*k
    print('Цена за', p,  cost, 'ryb')
    i += cost
    print('Общая стоимость', i, 'ryb')
    m[p][1] = (m[p][1]) - k
    # print(m)

    for key, values in m.items():
        print('Остаток',  key, '-'.join(str(num) for num in values), sep='-')
    s = input('Введите n для выхода: ')
    if s == 'n':
        break





# products = {"Рис": [1.2, 500], "Гречка": [1.4, 1000]}
# for key in products:
#     print(f"{key} - {products[key][0]} - {products[key][1]}")
# summ = 0
# name = ""
# while name != "n":
#     name = input("Введите название товара: ")
#     if name in products:
#         quantity = int(input("Введите количество: "))
#         products[name][1] = products[name][1] - quantity
#         summ += quantity * products[name][0]
#     elif name != "n":
#         print("Нет такого товара!")
#     if name == "n":
#         print("Покупка на сумму: ", round(summ, 2),'р.')
#         print("Остаток: ")
#         for key in products:
#             print(f"{key} - {products[key][1]}")





