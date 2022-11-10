class Animal:
    group = "Mammal"
    leg_count = 4
    category = "Domestic"
    sound = "bleat"
    name = "Goat"

    def print_animal_info(self):
        print("Animal: {", self.name, ",", self.group, ",", self.sound + "}")


class Cat(Animal):

    def __init__(self, name, group, sound):
        self.name = name
        self.group = group
        self.sound = sound


class Dog(Animal):
    name = "Dog"
    group = "Mammal"
    sound = "barks"


cow = Animal()
cow.print_animal_info()

cat = Cat("Cat", "Mammal", "meows")
cat.print_animal_info()

dog = Dog()
dog.print_animal_info()
