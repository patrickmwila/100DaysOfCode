from os import system, name


def clear():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("cls")
