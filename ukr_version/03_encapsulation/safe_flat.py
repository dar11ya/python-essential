# ПРИВАТНІ АТРИБУТИ
# Щоб створити приватний атрибут, треба написати два underscore __
from modern_flat import ModernFlat

class SafeFlat(ModernFlat):
    def __init__(self, number):
        super().__init__(number)
        self.__has_safe = True
        self.__safe_content = ["money", "document"]
        # self.__price = 100000

    def secure_item(self, unit, owner=False):
        if not self._check_owner(owner):
            return

        if unit.lower() not in self.__safe_content:
            self.__add_to_safe(unit)
        else:
            print(f"{unit.capitalize()} is already in the safe.")
            self.__display_safe_content

    @staticmethod
    def _check_owner(value):
        if not value:
            print("You can't complete operation")
        return bool(value)

    def __display_safe_content(self):
        print(f"Safe content for flat {self.number}: {self.__safe_content}")

    def __add_to_safe(self, unit):
        if self.__has_safe:
            self.__safe_content.append(unit)
            self.__display_safe_content()


    # def describe(self, friend=False, owner=False):
    #     description = (
    #         f"Flat {self.number} has {self.door_color} door color and"
    #         f" {self.electricity_readings} electricity count. \n"
    #     )
    #     friend_description = (
    #         f"Flat has {self._design} design and rooms count is {self._room_number} rooms."
    #         f"The flat has{' ' if self._has_tv else 'no' }TV. \n"
    #     )

        # owner_description = (
        #     f"The flat price is {self.__price} USD. The "
        #     f"flat has{' ' if self.__has_safe else ' no '}safebox. "
        #     f"The safe content is: "
        #     f"{', '.join(self.__safe_content) if self.__safe_content else 'empty'}."
        # )
        #
        # if friend:
        #     description += friend_description
        #
        # if owner:
        #     description += friend_description + owner_description
        #
        # print(description)

if __name__ == "__main__":
    flat = SafeFlat(212)

    flat.secure_item("camera", owner=True)
    flat.secure_item("money", owner=True)

    flat._check_owner(False)
    # flat.__add_to_safe("microphone") # AttributeError
    flat._SafeFlat__add_to_safe("microphone")

    # flat.describe()
    # flat.describe(friend=True)
    # flat.describe(owner=True)
    #
    # flat.__has_safe = False
    # flat.__safe_content = []
    # flat.__price = 200000
    # flat.describe(owner=True) # Інформація не переписалась. На Пайтоні є захист. Але є спосіб обійти і перевизначити їх, для цього  треба написати _НазваКласу__назваАтрибуту
    #
    # flat._SafeFlat__has_safe = False
    # flat._SafeFlat__safe_content = []
    # flat._SafeFlat__price = 200000
    # flat.describe(owner=True) # Тепер значення приватних атрибутів змінилось.
