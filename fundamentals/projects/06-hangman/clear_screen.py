from os import system, name
# '_' variable holds last expression in interpreter
# clear screen function


def clear():
    # mac and linux: os.name is 'posix'
    if name == "posix":
        _ = system("clear")

    else:
        # for windows
        _ = system("cls")
