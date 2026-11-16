"""Завдання: Звуки тварин
Створіть базовий клас Animal, який містить метод make_sound(), що повертає рядок "The animal
makes a sound".
Реалізуйте підкласи:
• Doп
• Перевизначає метод make_sound(), повертаючи "Woof-woof".
• Cat
• Перевизначає метод make_sound(), повертаючи "Meow".
• Cow
• Перевизначає метод make_sound(), повертаючи "Moo".
Створіть список об'єктів різних тварин та викличте метод make_sound() для кожного,
демонструючи поліморфізм у дії.
"""
import math

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"The animal makes a sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):

    def make_sound(self):
        return "Meow"

class Cow(Animal):

    def make_sound(self):
        return "Moo"

if __name__ == "__main__":
    dog = Dog("Arnold")
    cat = Cat("Garlfield")
    cow = Cow("Maryna")

    my_animals = [dog, cat, cow]
    for animal in my_animals:
        print(animal.make_sound())



"""Завдання 1: Поліморфізм через перевизначення методів
Створіть базовий клас Transport, який має метод move(), що повертає "The transport is moving".
Створіть підкласи Car, Bike та Airplane, які перевизначають метод move(), повертаючи відповідні
повідомлення:
• Car: "The car is driving".
• Bike: "The bike is riding".
• Airplane: "The airplane is flying"""

class Transport():
    def __init__(self, name):
        self.name = name

    def move(self):
        return "The transport is moving"

class Car(Transport):
    def move(self):
        return "The car is driving"

class Bike(Transport):
    def move(self):
        return "The bike is riding"

class Airplane(Transport):
    def move(self):
        return "The airplane is flying"

if __name__ == "__main__":
    car = Car("BMW")
    bike = Bike("Mitsubishi")
    airplane = Airplane("Boeing")
    my_vehicles = [car, bike, airplane]
    for my_vehicle in my_vehicles:
        print(my_vehicle.move())

"""Завдання 2: Поліморфізм через функції
Створіть класи Rectangle та Circle, кожен з яких має метод get_area(), що обчислює площу
відповідної фігури.
Напишіть функцію print_area(shape), яка приймає об'єкт будь-якої фігури та викликає його метод
get_area(), друкуючи результат у форматі:
"The area is: <значення>"."""

class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)

def print_area(shape):
    print(f"The area is: {shape.get_area()}")

rectangle = Rectangle(10, 5)
circle = Circle(10)
print_area(rectangle)
print_area(circle)

"""
Завдання 3: Поліморфізм через магічні методи
Створіть класи Vector2D та Vector3D, які представляють вектори у 2D та 3D просторах відповідно.
Реалізуйте для них магічний метод __add__(), який дозволяє складати вектори одного типу через
+.
Переконайтеся, що операція додавання працює коректно для двовимірних та тривимірних
векторів, наприклад:
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
result = v1 + v2
print(result) # Expected output: Vector2D(4, 6)
"""

class Vector2D:
    def __init__(self, v1_1, v1_2):
        self.v1_1 = v1_1
        self.v1_2 = v1_2

    def __add__(self, other):
        return Vector2D(
            self.v1_1 + other.v1_1,
            self.v1_2 + other.v1_2
        )

    def __str__(self):
            return f"Vector2D({self.v1_1}, {self.v1_2})"

class Vector3D:
    def __init__(self, v1_1, v1_2, v1_3):
        self.v1_1 = v1_1
        self.v1_2 = v1_2
        self.v1_3 = v1_3

    def __add__(self, other):
        return Vector3D(self.v1_1 + other.v1_1,
                        self.v1_2 + other.v1_2,
                        self.v1_3 + other.v1_3)

    def __str__(self):
        return f"Vector3D({self.v1_1}, {self.v1_2}, {self.v1_3})"

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2
print(v3)
v4 = Vector3D(1, 2, 3)
v5 = Vector3D(4, 5, 6)
v6 = v4 + v5
print(v6)



