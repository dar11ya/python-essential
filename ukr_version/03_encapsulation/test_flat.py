from safe_flat import SafeFlat

class TestFlat(SafeFlat):
    def test_access(self):
        print(f"Can access public attribute: {self.number=}")
        print(f"Can access protected attribute: {self._design=}")
        # print(f"Can access private attribute: {self.__price=}") # AttributeError
        print(f"Can access private attribute: {self._SafeFlat__price=}")


if __name__ == "__main__":
    flat = TestFlat(212)
    flat.describe(owner=True)

    flat.test_access()
