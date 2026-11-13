from lancelet import Lancelet

class Koala(Lancelet):
    habitation = "forest"
    support = "skeleton"

    def __init__(self, name, sleeping=False):
        super().__init__(name)
        self.sleeping = sleeping

    def eat(self, subject):
        if not self.sleeping:
            self.move("top")
            print(f"{self.name.capitalize()} climbs to the tree to eat {subject}")
        else:
            print(f"{self.name.capitalize()} cannot eat while sleeping")

    def change_state(self):
        if self.sleeping:
            print(f"{self.name.capitalize()} wakes up and sits on a branch")
        else:
            print(f"{self.name.capitalize()} lies on a branch and sleeps")

        self.sleeping = not self.sleeping

if __name__ == "__main__":
    print(Koala.describe())

    koala = Koala(name="Phascolarctos")
    koala.move("right")
    koala.eat("eucalyptus leaves")
    koala.change_state()
    koala.eat("eucalyptus leaves")
    koala.change_state()
