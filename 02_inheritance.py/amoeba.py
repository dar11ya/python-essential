# СПАДКУВАННЯ
# Повторення ООП та класів
""" Огляд спадкування:
    -Введення
    -Батьківські класи
    -Дочірні класи
    -Множинне спадкування"""

""" Спадкування(Inheritance) - це механізм, за допомогою якого один клас(дочірній клас, child class)
Може успадковувати атрибути та методи іншого класу(батьківського класу, parent class)"""

# Дочірній клас наслідує всі атрибути та методи батьківського класу
# Дочірній клас може додавати нові атрибути та методи або перевизначати існуючі

class Amoeba:
    organization = "single-cell"
    habitation = "water"

    def __init__(self, name):
        self.name = name

    @classmethod
    def describe(cls):
        return (f"{cls.__name__} has {cls.organization}"
                f"and lives in {cls.habitation}")

    @staticmethod
    def move(direction):
        print(f"Moves to the {direction} with pseudopodia")

    def eat(self, subject):
        print(f"{self.name.capitalize()} grows pseudopodis"
              f"to eat {subject}")

if __name__ == "__main__": # Дозволить нам не викликати зміст, того що ми напишемо до інших файлів у випадку імпортування
    print(Amoeba.describe())

    amoeba = Amoeba("proteus")
    amoeba.move("left")
    amoeba.eat("bacteria")