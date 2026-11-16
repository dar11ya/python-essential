# POLYMORPHISM
"""Lesson plan:
    - Review of OOP: classes, inheritance and encapsulation
    - Introduction to polymorphism
    - Using polymorphism in Python
    - Polymorphism through method overriding
    - Polymorphism through functions and operations
    - Polymorphism through magic methods
    - Summary"""

# Let's consider dogs and cats
# We know that a cat and a dog are animals and are able to make sounds. Although both dogs
# and cats can make sounds, these sounds differ significantly from each other. We can also train pets
# to make certain sounds on command, and the command can be the same for a dog and a cat.
# For example, the command "Speak" and the shared way of giving the command to dogs and cats can be called an
# interface for interacting with them. "Speak" is a common interface for handling the command.

"""Polymorphism is one of the core principles of OOP that allows objects of different classes to be handled
through a single interface. This lets methods, functions and operators perform operations on different objects and classes.

Advantages of polymorphism:
    - Flexibility (we can define which sounds different objects of a class will make without changing the interface of interaction)
    - Code reuse
    - Reduced complexity
    - Scalability"""

class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def speak():
        pass

class Dog(Animal):
    @staticmethod
    def speak():
        return "Woof"

class Cat(Animal):
    @staticmethod
    def speak():
        return "Meow"

if __name__ == "__main__":
    my_dog = Dog('Peter')
    my_cat = Cat('Garfield')

    my_animals = [my_dog, my_cat]
    for animal in my_animals:
        print(animal.speak())
