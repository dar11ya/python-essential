from flat import Flat

# To make protected attributes, put an underscore (_) before the attribute name
class ModernFlat(Flat):
    def __init__(self, number):
        super().__init__(number)
        self._room_number = 3
        self._design = "modern"
        self._has_tv = True

    def get_room_number(self, friend=False):  # The method is meant to be called only on behalf of a friend
        return self._room_number if friend else 0

    def get_design(self, friend=False):
        return self._design if friend else "undefined"

    def update_design(self, design, friend=False):
        if friend and design.startswith("modern"):
            self._design = design

    def turn_on_tv(self, friend=False):
        if friend and self._has_tv:
            print("TV turned on")
        else:
            print("TV not defined")

if __name__ == "__main__":
    flat = ModernFlat(212)

    flat.display_number()
    print(flat.get_design(friend=True))
    flat.update_design("modern warm", friend=True)
    print(flat.get_design(friend=True))

# Overriding the values of protected attributes is discouraged, but Python allows it
    flat._room_number = 5
    print(flat.get_room_number(friend=True))

    flat._design = "some design"
    print(flat.get_design(friend=True))

    flat._has_tv = False
    print(flat.turn_on_tv(friend=True))

# Protected attributes should be accessible only inside the class where we define them
# and inside child classes, but they should not be accessible to other entities.
# So the clients of these attributes are the class itself and its child classes.
