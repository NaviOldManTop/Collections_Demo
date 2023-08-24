def start_program() -> None:
    print("===================================")
    print("  Демонстрація стандартних колекцій")
    print("===================================")
    print("       1. Демонстрація кортежів    ")
    print("       2. Демонстрація множин      ")
    print("       3. Демонстрація словників   ")
    print("       4. Вихід із програми        ")
    print("===================================")


def finish_program() -> None:
    print("\nПрограму завершено", end="")


def allow_continue() -> bool:
    return input("\n> Продовжувати (y/n)? - ") == "y"

'''    quest = "\n> Продовжувати (y/n)? - "
    answer = input(quest)
    result = answer == "y"
    return result'''


def get_choice() -> int:
    return int(input("  Виберіть потрібну дію: "))