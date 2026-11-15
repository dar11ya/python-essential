import time

from modern_flat import ModernFlat

class ConnectedFlat(ModernFlat):
    def turn_on_tv(self, friend=False):
        if friend and self._has_tv:
            print("TV turned on")
            for _ in range(3):
                self._use_electricity(10)
                time.sleep(1)
            print("TV turned off")
        else:
            print("Not defined")

    def _use_electricity(self, count):  # Protected method. Calling it outside the class or its child classes is not recommended
        self.electricity_readings += count
        print(f"Increased electricity count by {count}.\n"
              f"Current electricity count: {self.electricity_readings}\n")

if __name__ == "__main__":
    flat = ConnectedFlat(
        212
    )

    flat.turn_on_tv(friend=True)
