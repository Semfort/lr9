# Loel var 2
print('start code …')
import json


operations_count = 0
with open('records.json', 'r', encoding='utf-8') as file:
            records = json.load(file)

def all_records():   
    global operations_count
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
    menu()

def one_records():
    global operations_count
    print("=" * 30)
    
    search_id = input("\nВведите ID для поиска: ")
    if search_id.isdigit() == True:
        pass
    else:
        print("Это не число!")
        one_records()
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
    menu()

def add_record():
    global operations_count
    print("=" * 30)
    
    print("Добавление новой записи:")
    new_id = input("Введите ID: ")
    if new_id.isdigit() == True:
        new_id = int(new_id)
    else:
        print("Это не число!")
        add_record()
    
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
        is_red_book_flower = input("Это растение в красной книге? Введите 1 - если да, введите 2 - если нет: ")
        price = input("Введите цену (число): ")
        if is_red_book_flower.isdigit() == True and price.isdigit() == True:
            is_red_book_flower = int(is_red_book_flower)
            price = int(price)
            if is_red_book_flower == 1:
                is_red_book_flower = True
            elif is_red_book_flower == 2:
                is_red_book_flower = False
            else:
                print("Неправильное число в четвёртом пункте!")
                add_record()
        else:
            print("Вы ввели не число в четвёртом или пятом пункте!")
            add_record()
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
    menu()

def del_record():
    global operations_count
    print("=" * 30)
    deleteid = input("Введите ID для удаления: ")
    if deleteid.isdigit() == True:
        deleteid = int(deleteid)
    else:
        print("Это не число!")
        del_record()
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
        confirm = input("Вы подтверждаете удаление? Введите 1 - если да, введите 2 - если нет: ")
        if confirm == "1" or confirm == "2":
            confirm = int(confirm)
            if confirm == 1:
                confirm = True
            elif confirm == 2:
                confirm = False
            else:
                print("Неправильное число!")
                del_record()
        else:
            print("Это не число!")
            del_record()
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
        menu()

def exit_program():
    global operations_count
    print(f"\nКоличество выполненных операций: {operations_count}")
    print('end code …')




def menu():
    global operations_count
    print('1 - Вывести все записи')
    print('2 - Вывести запись по полю ')
    print('3 - Добавить запись ')
    print('4 - Удалить запись по полю')
    print('5 - Выйти из программы\n')

    choice = input("Выберите пункт меню (1-5): ")
    if choice.isdigit() == True:
        choice = int(choice)
        if choice > 0 and choice < 6:
            pass
        else:
            print("Это неправильное число")
    else:
        print("Это не число!\n")
        menu()
    if choice == 1:
        all_records()

    elif choice == 2:
        one_records()

    elif choice == 3:
        add_record()

    elif choice == 4:
        del_record()

    elif choice == 5:
        exit_program()


menu()
