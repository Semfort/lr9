#Loel вар 2
print('start code …')
books = [
    {
        "title": "Война и мир",
        "author": "Лев Толстой", 
        "year": 1869
    },
    {
        "title": "Гарри Поттер и философский камень", 
        "author": "Джоан Роулинг",
        "year": 1997
    },
    {
        "title": "Мертвые души",
        "author": "Николай Гоголь",
        "year": 1842
    },
    {
        "title": "451° по Фаренгейту",
        "author": "Рэй Брэдбери", 
        "year": 1953
    },
    {
        "title": "Шерлок Холмс",
        "author": "Артур Конан Дойл",
        "year": 1887
    }
]

index = 1
for i in books:
    print(f"{'-' * 10} Книга {index} {'-' * 10} ")
    print(f"Название: {i['title']}, Автор: {i['author']},")
    print(f"{'-' * 10} {i['year']} {'-' * 10}\n")
    index+=1

print('end code …')