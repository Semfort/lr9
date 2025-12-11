#Loel вар 2
print('start code …')
import json
op = open('dump.json', 'r', encoding='utf-8')
data = json.load(op)
number = input("Введите номер квалификации: ").strip()
found = False


for i in data:
    if i.get('model') == 'data.skill':
        field = i.get('fields')
        if field.get('code') == number:
            found = True

            print("=" * 40, "Найдено", "=" * 40)
            print(f'{field.get('code','')} >> Специальность {field.get('title','')}, {field.get('c_type','')}') 
            break

if not found:
    print("=" * 40, "Не найдено", "=" * 40)

print('end code …')