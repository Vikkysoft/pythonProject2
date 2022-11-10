from collections import OrderedDict


def remove_repeated_character(my_string):
    return "".join(OrderedDict.fromkeys(my_string))


print(remove_repeated_character("Hello"))
print(remove_repeated_character("concatenate"))
print(remove_repeated_character("Professor"))
print(remove_repeated_character("Definite"))
print(remove_repeated_character("Committee"))