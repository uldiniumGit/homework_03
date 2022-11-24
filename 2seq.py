list_01 = []

elements = input('введите элементы списка через запятую, точку с запятой или слэш\n')

if ',' in elements:
    numbers = elements.split(',')
elif ';' in elements:
    numbers = elements.split(';')
elif '/' in elements:
    numbers = elements.split('/')
else:
    numbers = elements

for i in numbers:
    list_01.append(i)

list_no_duplicates = list(set(list_01))

print(list_no_duplicates)
