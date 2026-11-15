"""Task: Developing a class for working with a bank account
Create a BankAccount class:
• The class must have the following attributes:
• A public attribute account_holder (the account holder's name).
• A protected attribute _balance (the account balance).
• A private attribute __account_number (the account number).
• The class must have the following methods:
• A private method __generate_account_number() that generates a random
10-digit account number when a new object of the class is created.
• A public method deposit(amount: float) that lets you add the
specified amount to the account.
• A public method withdraw(amount: float) that lets you withdraw funds from the account
if there are enough funds on the account.
• A public method get_balance() that returns the current account balance.
• A public method get_account_number() that returns the account number
(using the private attribute).
Create an instance of the BankAccount class:
• Create a BankAccount object with the account holder's name.
• Use the deposit() and withdraw() methods to demonstrate working with the account
balance
• Call the get_balance() and get_account_number() methods to get the current balance
and the account number.
Access control:
• Try to access the protected attribute _balance and the private attribute
__account_number directly from the class object and show that this will cause an error
or is not recommended.
"""
# import random
#
#
# class BankAccount:
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self._balance = 0
#         self.__account_number = ""
#
#         self.__generate_account_number()
#
#     def __generate_account_number(self):
#         index = 0
#         while index < 10:
#             self.__account_number += str(random.randint(0, 9))
#             index += 1
#
#         print(f"Your account number is {self.__account_number}")
#
#     def deposit(self, amount: float):
#         if amount > 0:
#             self._balance += amount
#         print(f"You successfully deposited {amount}.")
#
#     def withdraw(self, amount: float):
#         if amount < 0 or self._balance < amount:
#             print("You cannot withdraw negative amount.")
#         else:
#             self._balance -= amount
#         print(f"You successfully withdrawn {amount}.")
#
#     def get_balance(self):
#         return self._balance
#
#     def get_account_number(self):
#         return self.__account_number
#
# if __name__ == '__main__':
#     bank_account = BankAccount('Daria')
#
#     bank_account.deposit(10)
#     bank_account.withdraw(6)
#     print(bank_account.get_balance())
#     print(bank_account.get_account_number())
#
#     print(bank_account._balance)
#     print(bank_account._BankAccount__account_number)

"""Task 1: Implementing a class for handling student data
Create a Student class with the attributes name (the student's name), _grades (a list of grades, a protected
attribute) and a private attribute __id (the student's unique identifier). Implement methods for
adding a grade (add_grade()), getting the average grade (get_average_grade()) and printing
student information (print_details())."""

# class Student:
#     def __init__(self, name, grades, id):
#         self.name = name
#         self._grades = grades
#         self.__id = id
#
#     def add_grade(self, grade):
#         self._grades.append(grade)
#
#     def get_average_grade(self):
#         return sum(self._grades) / len(self._grades)
#
#     def print_details(self):
#         print(f"The student name is {self.name}. The student grades are {self._grades}. The student id is {self.__id}.")
#
# student = Student(name='Maryna', grades=[12, 10, 8, 11, 12], id=1212)
# student.print_details()
# print(student.get_average_grade())
# student.add_grade(10)
# student.print_details()
# print(student.get_average_grade())

"""Task 2: Implementing a class for managing products in a store
Create a Product class with the attributes name, price (a protected attribute) and a private attribute
__sku (the product's unique code). Implement methods for setting the price (set_price()), getting
the price (get_price()) and printing product information (print_details())."""

# class Product:
#     def __init__(self, name, price, sku):
#         self.name = name
#         self._price = price
#         self.__sku = sku
#
#     def set_price(self, price):
#         self._price = price
#
#     def get_price(self):
#         return self._price
#
#     def print_details(self):
#         print(f"The product {self.__sku} called {self.name} and has price {self._price}")
#
# if __name__ == "__main__":
#     product = Product(
#         name="bread",
#         price=10,
#         sku=1010
#     )
#
#     product.set_price(20)
#     product.get_price()
#     product.print_details()

"""Task 3: Implementing a class for managing vehicles
Create a Vehicle class with the attributes mark (make), model and a protected attribute
_mileage (the mileage). Add methods for updating the mileage (update_mileage()), getting the mileage
(get_mileage()) and printing vehicle information (print_details())."""

# class Vehicle:
#     def __init__(self, mark, model, mileage):
#         self.mark = mark
#         self.model = model
#         self._mileage = mileage
#
#     def update_mileage(self, new_mileage):
#         self._mileage = new_mileage
#
#     def get_mileage(self):
#         return self._mileage
#
#     def print_details(self):
#         print(f"The car mark is {self.mark}, model is {self.model}, mileage is {self._mileage}")
#
# if __name__ == "__main__":
#     car = Vehicle(
#         mark="BMW",
#         model="x6",
#         mileage=20000
#     )
#
#     car.update_mileage(18000)
#     print(car.get_mileage())
#     car.print_details()
