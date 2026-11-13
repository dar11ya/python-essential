from lancelet import Lancelet

class Clownfish(Lancelet):
    support = "skelet"

    def __init__(self, name, feeding_type, water_type):
        super().__init__(name)
        self.feeding_type = feeding_type
        self.water_type = water_type
        self.hidden = False

    def hide(self, place):
        self.hidden = True
        print(f"{self.name.capitalize()} hides in the {place} being in the {self.water_type}"
              f"water")

    def reveal(self):
        self.hidden = False
        self.move("forward")

    def eat(self, subject):
        print(f"{self.name.capitalize()} eats {subject} since it is {self.feeding_type}")

if __name__ == "__main__":
    print(Clownfish.describe())

    clownfish = Clownfish(
        name="Amphiberion",
        feeding_type="amniverous",
        water_type="salt"
    )

    clownfish.move("left")
    clownfish.eat("zooplankton")
    clownfish.hide("anemone")
    clownfish.reveal()

    print(f"Clownfish is {"resting" if clownfish.hidden else "swimming"}")