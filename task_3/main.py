# Loel var 2
print('start code …')
import json


operations_count = 0

with open('records.json', 'r', encoding='utf-8') as file:
            records = json.load(file)

while True:
    print('1 - Вывести все записи')
    print('2 - Вывести запись по полю ')
    print('3 - Добавить запись ')
    print('4 - Удалить запись по полю')
    print('5 - Выйти из программы\n')

    choice = int(input("Выберите пункт меню (1-5): "))
    if choice == 1:
        print("=" * 30)
        
        print("Все записи:")
        for i in records:
            print("-" * 20) 
            #for j,k in i.items():
                #print(j, ": ", k)
            print("ID цветка: ", i.get("id"))
            print("Имя цветка: ", i.get("name"))
            print("Латинское название цветка: ", i.get("latin_name"))
            if i.get("is_red_book_flower") == True:
                print("Цветок в Красной книге")
            else:
                print("Цветок не в Красной книге")
            print("Цена цветка: ", i.get("price"))
        print("=" * 30)
        operations_count += 1


    elif choice == 2:
        print("=" * 30)
        
        search_id = input("\nВведите ID для поиска: ")
        found_id = 0
        found = False
        for i in records:
            if i.get("id") == search_id:
                print("\nЗапись найдена:")
                found = True
                #for j,k in i.items():
                    #print(j, ": ", k)
                print("ID цветка: ", i.get("id"))
                print("Имя цветка: ", i.get("name"))
                print("Латинское название цветка: ", i.get("latin_name"))
                if i.get("is_red_book_flower") == True:
                    print("Цветок в Красной книге")
                else:
                    print("Цветок не в Красной книге")
                print("Цена цветка: ", i.get("price"))
                print("Позиция цветка: ", found_id)
                break
            found_id+=1
        if found == False:
            print("Запись не найдена!")
        print("=" * 30)
        operations_count += 1


    elif choice == 3:
        print("=" * 30)
        
        print("Добавление новой записи:")
        new_id = int(input("Введите ID: "))

        idexists = False
        for i in records:
            if i.get("id") == new_id:
                idexists = True
                break
        if idexists == True:
                print(f"Ошибка: запись с ID {new_id} уже существует!")
        else:
            name = input("Введите имя цветка: ")
            latin_name = input("Введите латинское название: ")
            is_red_book_flower = False
            is_red_book_flower = int(input("Это растение в красной книге? Введите 1 - если да, введите 2 - если нет: ")) == 1
            price = int(input("Введите цену (число)"))

            new_record = {
                "id": new_id,
                "name": name,
                "latin_name": latin_name,
                "is_red_book_flower": is_red_book_flower,
                "price": price
            }

        records.append(new_record)
        with open('records.json', 'w', encoding='utf-8') as file:
            json.dump(records, file, ensure_ascii=False)
                
        print("Запись успешно добавлена!")
        print("=" * 30)
        operations_count += 1


    elif choice == 4:
        print("=" * 30)
        deleteid = int(input("Введите ID для удаления: "))
         
        found = False
        found_id = 0
        for i in records:
            if i.get("id") == deleteid:
                print("\nЗапись найдена:")
                found = True
                #for j,k in i.items():
                    #print(f"{j}: {k}")
                print("ID цветка: ", i.get("id"))
                print("Имя цветка: ", i.get("name"))
                print("Латинское название цветка: ", i.get("latin_name"))
                if i.get("is_red_book_flower") == True:
                    print("Цветок в Красной книге")
                else:
                    print("Цветок не в Красной книге")
                print("Цена цветка: ", i.get("price"))
                break
            found_id+=1
        
        if found == False:
            print("Запись не найдена!")
        else: 
            confirm = False
            confirm = input("Вы подтверждаете удаление? Введите 1 - если да, введите 2 - если нет: ") == "1"

            if confirm == True:
                del records[found_id]

                with open('records.json', 'w', encoding='utf-8') as file:
                    json.dump(records, file, ensure_ascii=False)

                print("Запись успешно удалена!")
                operations_count += 1
            else:
                print("Удаление отменено.")
            print("=" * 30)
            operations_count += 1

    elif choice == 5:
        print(f"\nКоличество выполненных операций: {operations_count}")
        break

print('end code …')