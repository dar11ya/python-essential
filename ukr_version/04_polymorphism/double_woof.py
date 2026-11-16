"""Перевизначення методів(Method overriding) - дозволяє підкласу надати специфічну реалізацію методу, що вже визначений у базовому класі
Це дозволяє різним класам мати різну реалізацію одного і того ж методу"""

from animals import Dog, Cat


class DoubleWoofDog(Dog):
    @staticmethod
    def speak():
        return "Woof Woof"

if __name__ == '__main__':
    cat = Cat("Garlfield")
    dog_one = Dog('Peter')
    dog_two = DoubleWoofDog('Arnold')

    my_animals = [cat, dog_one, dog_two]
    for animal in my_animals:
        print(animal.speak())
