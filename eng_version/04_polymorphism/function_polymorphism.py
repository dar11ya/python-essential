# Functions can work with objects of different classes by using polymorphism
# Overridden methods can provide polymorphic behavior

from double_woof import DoubleWoofDog, Dog, Cat

def describe_pet(pet):
    print(f"Pet's name is {pet.name.title()} "
          f"and it says {pet.speak()}")


if __name__ == '__main__':
    cat = Cat("Garfield")
    dog_one = Dog('Peter')
    dog_two = DoubleWoofDog('Arnold')

    my_animals = [cat, dog_one, dog_two]
    for animal in my_animals:
        describe_pet(animal)
