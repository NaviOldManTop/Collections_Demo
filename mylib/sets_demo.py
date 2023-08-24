"""
    Множина - це неевпрорядкована змінювання колекція унікальних даних,
    яка підтримую стандартні математичні операції із множинами
    ===================================================================
"""


def create_sets() -> None:
    set1 = {10, 20, 30, 40, 50, 60, 70}
    print(set1)
    set2 = {10, 20, 20, 30, 30, 30}
    print(set2)
    persons = ["Ivan", "Mykola", "Petro", "Alex", "Ivan", "Petro", "Alex", "Alex"]
    print(persons)
    buff = set(persons)
    names = list(buff)
    print(names)


def sets_operations() -> None:
    persons = set()

    print(" ")
    print("1. Додавання елементів: ")
    persons.add("Vasyl")
    persons.add("Petro")
    persons.add("Mykola")
    persons.add("Svitlana")
    persons.add("Maryna")
    print(persons)

    print(" ")
    print("2. Видалення елементів")
    print(" # 1")
    name = "Mykola"
    if name in persons:
        persons.remove(name)
    print(persons)

    print(" ")
    print(" # 2 ")
    persons.discard("Maryna")
    print(persons)

    print(" ")
    print("3. Перебір елементів:")
    for item in persons:
        print(f"   . {item}")


def sets_methods() -> None:
    pass