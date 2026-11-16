# Функції можуть працювати з об'єктами різних класів, використовуючи поліморфізм
# Перевизначені методи можуть забезпечити поліморфну поведінку

from double_woof import DoubleWoofDog, Dog, Cat

def describe_pet(pet):
    print(f"Pet's name is {pet.name.title()}"
          f"and it says {pet.speak()}")


if __name__ == '__main__':
    cat = Cat("Garlfield")
    dog_one = Dog('Peter')
    dog_two = DoubleWoofDog('Arnold')

    my_animals = [cat, dog_one, dog_two]
    for animal in my_animals:
        describe_pet(animal)
