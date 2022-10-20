def start():
    start = int(input("Введите 1, если хотите ввести данные, 2 - если получить: "))
    while start<1 or start>2:
        print("Введите число от 1 до 2")
        try:
            start = int(input("Введите 1, если хотите ввести данные, 2 - если получить: "))
        except ValueError:
            print("Введите корректное число")
    return start