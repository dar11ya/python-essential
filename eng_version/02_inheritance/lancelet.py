from amoeba import Amoeba

class Lancelet(Amoeba):  # Lancelet inherits from Amoeba
    organization = "multi-cell"
    support = "notochord"

    @classmethod
    def describe(cls):
        description = super().describe()  # super() lets us access the parent class
        return description + f". It has {cls.support} for support."

    @staticmethod
    def move(direction):
        print(f"Move to the {direction} with muscles.")

    def eat(self, subject):
        print(f"{self.name.capitalize()} filters water to eat {subject}")

if __name__ == "__main__":
    print(Lancelet.describe())

    lancelet = Lancelet("Amphioxus")
    lancelet.move("right")
    lancelet.eat("organic particles")

"""If we comment out `if __name__ == "__main__"` in amoeba.py, running lancelet.py
will also print the Amoeba demo output, which shouldn't be printed here"""
