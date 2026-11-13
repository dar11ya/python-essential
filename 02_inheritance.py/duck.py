# Множинне спадкування

class Flyer:
    @staticmethod
    def fly():
        print("Flying")

class Swimmer:
    @staticmethod
    def swim():
        print("Swimming")

class Duck(Flyer, Swimmer):
    @staticmethod
    def quack():
        print("Quacking")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()