list_01 = []

count = int(input('введите количество элементов списка\n'))

for i in range(count):
    x = input(f'введите элемент {i + 1}\n')
    list_01.append(x)

list_01.sort()

print(list_01)
