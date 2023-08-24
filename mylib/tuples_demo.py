"""
    Кортежі - це впорядковані, але не змінювані набори данних
    =========================================================
"""


def tuples_create_demo() -> None:
    print("\n>  Способи створення кортежів: ")
    print("  ------------------------------")

    print("  1. За допомогою круглих дужок:")
    student1 = ("Василь Пупченко", 21, "Київ", 7.5)
    print(" ", type(student1), student1)

    print("  2. За допомогою перелічення (без дужок):")
    student2 = "Ліза Пупченко", 19, "Львів", 10.5
    print(" ", type(student2), student2)

    print("  3. За допомогою конструктора (із списку):")
    student3 = tuple(["Микола Пупченко", 27, "Житомир", 8.5])
    print(" ", type(student3), student3)

    print("  4. Кортеж із одного елементу:")
    email = ('vasil#gmail.com',)
    print(" ", type(email), email)


def tuples_operations_demo() -> None:
    print("\n>  Базові операції із кортежами: ")
    print("  ------------------------------")

    names = "Tom", "Bob", "Kate", "John", "Jack"
    print("", names)

    print(" ")
    print("  1. Доступ до елементів за їх індексом:")
    print("   ", names[0])
    print("   ", names[-1])

    print(" ")
    print("  2. Зрізи елементів за їх індексом:")
    print("   ", names[:3])
    print("   ", names[1:-1])

    print(" ")
    print("  3. Цикл перебору за індексами:")
    for i in range(len(names)):
        print(f"    {i + 1} - {names[i]}")

    print(" ")
    print("  4. Цикл перебору за елементами:")
    for elem in names:
        print(f"    {elem}")

    print(" ")
    print("  5. Перевірка існування елементів:")
    name = input("  Введіть ім'я: ")
    if name in names:
        print("  Така людина є в кортежі, ЮХУУ!")
    else:
        print("  На жаль, така людина в кортежі не знайдена.")


def tuples_methods_demo() -> None:
    print("\n>  Методи кортежів: ")
    print("  ------------------------------")
    users = "Tom", "Bob", "Kate", "John", "Jack"

    print("  1. Пошук позицій елементу у кортежі: ")
    user = input("     Введіть користувача: ")
    if user in users:
        i = users.index(user)
        print(f"    Користувач - знайдений, {i + 1} по порядку")
    else:
        print("     Користувач не знайдений!")

    print(" ")
    print("  2. Пошук кількості елементів у кортежі: ")
    numbers = 100, 300, 500, 700, 100, 200, 500, 500
    item = int(input("     Введіть число яке хочете перевірити: "))
    k = numbers.count(item)
    print(f"     Данне число зустрічається {k} р.")


def tuples_unpack_demo() -> None:
    print("\n>  Деструктуризація (розпаковка) кортежів: ")
    print("  ------------------------------------------")
    users = "Tom", "Bob", "Kate", "John", "Jack"
    students = (
        "Tom, 21, 7.5",
        "Bob, 25, 8.5",
        "Kate, 19, 11.5",
        "John, 45, 10.4",
        "Jack, 37, 8.6"
    )
    # ->
    tom, bob, kate, john, jack = students
    print(f"    Tom: {tom}")
    print(f"    Bob: {bob}")
    print(f"    Kate: {kate}")
    print(f"    John: {john}")
    print(f"    Jack: {jack}")