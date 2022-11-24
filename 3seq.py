list_01 = []
list_02 = []

# Наполняем первый список
count = int(input('введите количество элементов первого списка\n'))

for i in range(count):
    x = input(f'введите элемент {i + 1}\n')
    list_01.append(x)

# Наполняем второй список
count = int(input('введите количество элементов второго списка\n'))

for i in range(count):
    x = input(f'введите элемент {i + 1}\n')
    list_02.append(x)

# Убираем из первого списка элементы, которые присутствуют во втором списке
list_01 = [x for x in list_01 if x not in list_02]

print(list_01)
