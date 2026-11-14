# INHERITANCE
# Review of OOP and classes
""" Overview of inheritance:
    -Introduction
    -Parent classes
    -Child classes
    -Multiple inheritance"""

""" Inheritance is a mechanism by which one class (a child class)
can inherit the attributes and methods of another class (a parent class)"""

# A child class inherits all attributes and methods of its parent class
# A child class can add new attributes and methods or override existing ones

class Amoeba:
    organization = "single-cell"
    habitation = "water"

    def __init__(self, name):
        self.name = name

    @classmethod
    def describe(cls):
        return (f"{cls.__name__} has {cls.organization} organization "
                f"and lives in {cls.habitation}")

    @staticmethod
    def move(direction):
        print(f"Moves to the {direction} with pseudopodia")

    def eat(self, subject):
        print(f"{self.name.capitalize()} grows pseudopodia "
              f"to eat {subject}")

if __name__ == "__main__":  # Keeps this block from running when the file is imported into other files
    print(Amoeba.describe())

    amoeba = Amoeba("proteus")
    amoeba.move("left")
    amoeba.eat("bacteria")
