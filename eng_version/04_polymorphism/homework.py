"""Task: Animal sounds
Create a base class Animal with a make_sound() method that returns the string "The animal
makes a sound".
Implement the subclasses:
• Dog
• Overrides the make_sound() method, returning "Woof-woof".
• Cat
• Overrides the make_sound() method, returning "Meow".
• Cow
• Overrides the make_sound() method, returning "Moo".
Create a list of objects of different animals and call the make_sound() method on each of them,
demonstrating polymorphism in action.
"""
import math

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"The animal makes a sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof-woof"

class Cat(Animal):

    def make_sound(self):
        return "Meow"

class Cow(Animal):

    def make_sound(self):
        return "Moo"

if __name__ == "__main__":
    dog = Dog("Arnold")
    cat = Cat("Garfield")
    cow = Cow("Maryna")

    my_animals = [dog, cat, cow]
    for animal in my_animals:
        print(animal.make_sound())


"""Task 1: Polymorphism through method overriding
Create a base class Transport with a move() method that returns "The transport is moving".
Create the subclasses Car, Bike and Airplane that override the move() method, returning the corresponding
messages:
• Car: "The car is driving".
• Bike: "The bike is riding".
• Airplane: "The airplane is flying"."""

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

"""Task 2: Polymorphism through functions
Create the classes Rectangle and Circle, each with a get_area() method that calculates the area
of the corresponding shape.
Write a function print_area(shape) that takes an object of any shape and calls its
get_area() method, printing the result in the format:
"The area is: <value>"."""

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
Task 3: Polymorphism through magic methods
Create the classes Vector2D and Vector3D that represent vectors in 2D and 3D space respectively.
Implement the magic method __add__() for them, which allows adding vectors of the same type with
+.
Make sure the addition works correctly for two-dimensional and three-dimensional
vectors, for example:
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
