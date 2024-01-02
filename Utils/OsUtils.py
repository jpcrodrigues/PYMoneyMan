from os import system, name


def clear():
    if name == 'nt':  # for linux
        system('cls')
    else:  # for linux or mac
        system('clear')
