from amoeba import Amoeba

class Lancelet(Amoeba): # Ланцет наслідується від амеби
    organization = "multi-cell"
    support = "notochord"

    @classmethod
    def describe(cls):
        description = super().describe() # За допомогою супер ми можемо звернутись до батьківського класу
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

"""Якщо ми закоментуємо у amoeba.py if __name__ == "__main__", то при виводі файлу lancelet.py
у нас виведеться ще частина з amoeba, яка не має вже виводитись"""