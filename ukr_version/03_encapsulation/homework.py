"""Завдання: Розробка класу для роботи з банківським рахунком
Створити клас BankAccount:
• Клас повинен мати наступні атрибути:
• Публічний атрибут account_holder (ім'я власника рахунку).
• Захищений атрибут _balance (баланс рахунку).
• Приватний атрибут __account_number (номер рахунку).
• Клас повинен мати наступні методи:
• Приватний метод __generate_account_number(), який генерує випадковий номер
рахунку довжиною 10 цифр при створенні нового об'єкту класу.
• Публічний метод deposit(amount: float), який дозволяє поповнювати рахунок на
вказану суму.
• Публічний метод withdraw(amount: float), який дозволяє знімати кошти з рахунку,
якщо достатньо коштів на рахунку.
• Публічний метод get_balance(), який повертає поточний баланс рахунку.
• Публічний метод get_account_number(), який повертає номер рахунку
(використовуючи приватний атрибут).
Створити екземпляр класу BankAccount:
• Створити об'єкт класу BankAccount з ім'ям власника рахунку.
• Використати методи deposit() та withdraw(), щоб продемонструвати роботу з балансом
рахунку
• Викликати методи get_balance() та get_account_number(), щоб отримати поточний баланс
та номер рахунку.
Контроль доступу:
• Спробувати отримати доступ до захищеного атрибуту _balance та приватного атрибуту
__account_number безпосередньо з об'єкта класу та показати, що це викличе помилку
або не рекомендується.
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

"""Завдання 1: Реалізація класу для обробки даних студентів
Створіть клас Student, який має атрибути name (ім'я студента), _grades (список оцінок, захищений
атрибут) та приватний атрибут __id (унікальний ідентифікатор студента). Реалізуйте методи для
додавання оцінки (add_grade()), отримання середньої оцінки (get_average_grade()) та виведення
інформації про студента (print_details())."""

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

"""Завдання 2: Реалізація класу для керування продуктами в магазині
Створіть клас Product, який має атрибути name, price (захищений атрибут) та приватний атрибут
__sku (унікальний код товару). Реалізуйте методи для встановлення ціни (set_price()), отримання
ціни (get_price()) та виведення інформації про продукт (print_details())."""

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

"""Завдання 3: Реалізація класу для керування транспортними засобами
Створіть клас Vehicle, який має атрибути mark (марка), model (модель) та захищений атрибут
_mileage (пробіг). Додайте методи для оновлення пробігу (update_mileage()), отримання пробігу
(get_mileage()) та виведення інформації про транспортний засіб (print_details())."""

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
