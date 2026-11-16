"""Магічні методи(magic methods) починаються і закінчуються двома підкресленнями (наприклад, __str__, __add__).
 Поліморфізм дозволяє перевизначити ці методи для підтримки різної поведінки у різних класах"""

from function_polymorphism import (
    Dog,
    DoubleWoofDog,
    describe_pet
)

class MagicDog(Dog):
    def __add__(self, other):
        return MagicDog(f"Puppy (love of {self.name}"
                        f"and {other.name})")

    def __str__(self):
        return f"{self.name} (Magic Dog)"

if __name__ == "__main__":
    dog_one = MagicDog("Peter")
    dog_two = MagicDog("Alice")
    dog_three = dog_two + dog_one
    dog_four = DoubleWoofDog("Arnold")

    my_animals = [dog_one, dog_two, dog_three, dog_four]
    for animal in my_animals:
        print(animal)

    for animal in my_animals:
        describe_pet(animal)
