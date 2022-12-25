print(*(i for i in (input() for _ in range(int(input()))) if "лук" not in i.lower()), sep=", ")
