"""План курсу:
1. Введення в ООП: огляд класів
2. Спадкування
3. Інкапсуляція
4. Поліморфізм
5. Абстракція
6. Робота з рекурсією
7. Структури даних
8. Модулі Python
9. Читання та запис файлів
10. Парадигми програмування та стандарти оформлення коду"""

# Введення в ООП: огляд класів
"""Все навколо нас - об'єкти. Різні об'єкти можна об'єднати у категорії. Наприклад серед об'єктів можна виділити клас 
літаючих апаратів, куда будуть входити багато літаючих апаратів) Серед цим апаратів існують різні типи літаків, наприклад 
з одним двигуном, з двома двигунами. Серед всіх літаків можна виділити клас пасажирських літаків. Всі пасажирські літаки 
є літальними апаратами, але не всі літальні апарати є пасажирськими літаками."""

"""Існують матеріальні та нематеріальні об'єкти. Нематеріальні - музика, пісні, процеси та ідеї, кіно та відео. Ми можемо
виділяти нематеріальні об'єкти у категорії. Існує багато жанрів музики. Музика може створюватись з-за допомогою нот щоб 
грати під час концертів або з-за допомогою програмного забезпечення, щоб зберігати і відтворювати її. Так само можна з 
матеріальними об'єктами, ми можемо креслити ці об'єкти, що допоможе нам мати розуміння які саме складов треба об'єднати 
і як саме щоб утворити об'єкт. Тож побудова літака відбувається поступово. Спочатку креслення, потім беруться матеріали,
які об'єднуються і так виходить літак. Причому один шаблон креслення може слугувати для будови різних літаків. """

"""У ООП креслення - це клас(class), а кінцевий результат, що створюється - об'єкт/екземпляр класу(instance)"""

"""Клас та екземпляр класу є нематеріальними і вони зберігаються у оперативній пам'яті комп'ютера(RAM)"""

"""У літака є такі властивості: є боковий текст, є основний колір, додатковий колір, к-сть бокових дверей - 5, наявний 
пілот, значить він не є автопілотованим. Спробуємо його створити як об'єкт класу"""
"""__init__ - це конструктор класу і він зазначає які саме властивості матиме екземпляр класу, що буде створений з відповідного
класу. використання def всередині класу наз - метоами, а не функціями!"""

"""Перший аргумент є self. Він дозволяє звертатись до екземпляра класу, під час його побудови"""

# class Plane:
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text #Ми створюємо властивість, яка наз side_text, вона буде доступна після створення екземпляра класу
#         self.main_color = main_color
#         self.additional_colors = additional_colors
#         self.side_doors_colors = side_doors_colors
#         self.autopilot = autopilot


# boeing = Plane(
#     side_text="Southwind",
#     main_color="white",
#     additional_colors=["red"],
#     side_doors_colors=5,
#     autopilot=False
# )

# print(boeing.side_text)

"""Якщо ми спробуємо викликати Plane.side_text - це буде Error"""

# airbus = Plane(
#     side_text="Delta",
#     main_color="white",
#     additional_colors=["red", "blue"],
#     side_doors_colors=4,
#     autopilot=False
# )

# print(f"Additional colors: {airbus.additional_colors}")

"""Літак може зілатати і сідати. Ці властивості можна описати за допомогою інстанс методів класів."""
#
# class Plane:
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text
#         self.main_color = main_color
#         self.additional_colors = additional_colors
#         self.side_doors_colors = side_doors_colors
#         self.autopilot = autopilot
#
#     def take_off(self):  # Додали інстанс метод для зльоту
#         print(f"{self.side_text} takes off")
#
#     def land(self): # Додали інстанс метод для посадки
#         print(f"{self.side_text} lands")
#
# airbus = Plane(
#     side_text="Delta",
#     main_color="white",
#     additional_colors=["red", "blue"],
#     side_doors_colors=4,
#     autopilot=False
# )
#
# boeing = Plane(
#     side_text="Southwind",
#     main_color="white",
#     additional_colors=["red"],
#     side_doors_colors=5,
#     autopilot=False
# )
#
#
# airbus.take_off()
# airbus.land()
#
# boeing.take_off()
# boeing.land()

"""Деякі властивості можуть зберігатися для всіх літаків та бути заздалегідь передбачені кресленням, наприклад тип двигунів.
Example: Тип двигуна: турбовентиляторний"""

# class Plane:
#     engine_type = "Turbofan" # Це класовий атрибут. Діє для всіх.
#
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text
#         self.main_color = main_color
#         self.additional_colors = additional_colors
#         self.side_doors_colors = side_doors_colors
#         self.autopilot = autopilot
#
#     def take_off(self):  # Додали інстанс метод для зльоту
#         print(f"{self.side_text} takes off")
#
#     def land(self): # Додали інстанс метод для посадки
#         print(f"{self.side_text} lands")
#
# print(f"Type: {Plane.engine_type}")

"""КЛАСОВІ МЕТОДИ"""
"""Щоб позначити що це не ініт метод, а класовим, ми використовуємо спец декоратор  @classmethod він додає нові властивості.
В нашому випадку це те що ми першим аргументом приймаємо не self а власний клас"""
"""Класові методи ми можемо викликати напряму від класів"""

# class Plane:
#     engine_type = "Turbofan" # Це класовий атрибут. Діє для всіх.
#
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text
#         self.main_color = main_color
#         self.additional_colors = additional_colors
#         self.side_doors_colors = side_doors_colors
#         self.autopilot = autopilot
#
#     @classmethod
#     def inspect_engine(cls):
#         print(f"Plane has {cls.engine_type} engine")
#
#     def take_off(self):
#         print(f"{self.side_text} takes off")
#
#     def land(self):
#         print(f"{self.side_text} lands")
#
# Plane.inspect_engine()

# СТАТИЧНІ МЕТОДИ
"""Можемо викликати як від класів, так і від екземплярів класу"""
"""Припустимо, що ми хочемо робити підрахунок споживання палива на певну дистанцію.
Маємо такі витрати на 1000км польоту:
-Літак витрачає за годину 7т палива
-При крейсерській швидкості він пролітає 900км за год
-За 1000км літак використовує (7000х1000) / 900 = ~7778 кг палива"""

# class Plane:
#     engine_type = "Turbofan" # Це класовий атрибут. Діє для всіх.
#
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text
#         self.main_color = main_color
#         self.additional_colors = additional_colors
#         self.side_doors_colors = side_doors_colors
#         self.autopilot = autopilot
#
#     @classmethod
#     def inspect_engine(cls):
#         print(f"Plane has {cls.engine_type} engine")
#
#     @staticmethod
#     def calculate_fuel(distance):
#         hour_fuel = 7000
#         hour_distance = 900
#         fuel = (hour_fuel * distance) / hour_distance
#         print(f"For {distance} km plane need {int(fuel)} kg of fuel")
#
#     def take_off(self):
#         print(f"{self.side_text} takes off")
#
#     def land(self):
#         print(f"{self.side_text} lands")
#
# airbus = Plane(
#     side_text="Delta",
#     main_color="white",
#     additional_colors=["red", "blue"],
#     side_doors_colors=4,
#     autopilot=False
# )
#
# boeing = Plane(
#     side_text="Southwind",
#     main_color="white",
#     additional_colors=["red"],
#     side_doors_colors=5,
#     autopilot=False
# )
#
# Plane.calculate_fuel(1000)
# boeing.calculate_fuel(3500)
# airbus.calculate_fuel(3300)

# HOMEWORK
"""
Завдання: Розробка класу для керування замовленнями
Створіть клас Order, який буде моделювати замовлення в інтернет-магазині. Клас повинен мати
наступні характеристики та методи:
• Атрибути класу:
• order_id (ціле число) - унікальний ідентифікатор замовлення.
• customer_name (рядок) - ім'я клієнта, що робить замовлення.
• items (список рядків) - список товарів у замовленні.
• Методи класу:
• __init__(self, order_id, customer_name): Конструктор класу, який приймає order_id і
customer_name та ініціалізує атрибути.
• add_item(self, item): Додає товар до списку items.
• remove_item(self, item): Видаляє вказаний товар зі списку items, якщо він
присутній.
• print_order_details(self): Виводить деталі замовлення, включаючи order_id,
customer_name та список товарів.
• Завдання для виконання:
• Створіть об'єкт класу Order з довільним order_id і customer_name.
• Додайте декілька товарів до замовлення за допомогою методу add_item.
• Видаліть один або декілька товарів за допомогою методу remove_item.
• Виведіть деталі замовлення за допомогою методу print_order_details.
"""
#
# class Order:
#
#     def __init__(self, order_id, customer_name):
#         self.order_id = order_id
#         self.customer_name = customer_name
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print("You can't remove this item.")
#
#     def print_order_details(self):
#         print(f"The order number {self.order_id} for {self.customer_name} contains {self.items}.")
#
#
# first_order = Order(
#     order_id=1234,
#     customer_name='Mark'
# )
#
# first_order.add_item(item="bread")
# first_order.add_item(item="cheese")
# first_order.add_item(item="milk")
# first_order.remove_item(item="potato")
# first_order.print_order_details()

"""
Реалізація класу для керування книгами в бібліотеці
Створіть клас Book, який має атрибути title, author, genre та status (доступна/вибрана). Додайте 
методи для видачі книги (borrow_book()), повернення книги (return_book()) та виведення
інформації про книгу (print_details()).
"""

# class Book:
#     def __init__(self, title, author, genre, status):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.status = status
#
#     def borrow_book(self):
#         if self.status == "доступна":
#             print(f"You borrowed {self.title}")
#             self.status = "недоступна"
#         else:
#             print("This book is unavailable")
#
#     def return_book(self):
#         self.status = "доступна"
#
#     def print_details(self):
#         print(f"The book called {self.title} by {self.author} is {self.genre} and is {self.status}")
#
# book1 = Book(
#     title="1984",
#     author="George Orwell",
#     genre="Dystopian fiction",
#     status="доступна"
# )
#
# book1.borrow_book()
# book1.return_book()
# book1.print_details()

"""Реалізація класу для керування банківським рахунком
Створіть клас BankAccount, який має атрибути account_number, account_holder, balance. Реалізуйте
методи для зняття коштів (withdraw()), внесення коштів (deposit()), перевірки балансу
(check_balance()) та виведення інформації про рахунок (print_account_details())."""

# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("You cannot withdraw more than you have")
#         else:
#             self.balance -= amount
#             print(f"You withdrew {amount} from {self.account_holder}, now your balance is {self.balance}")
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"You successfully deposit {amount} from {self.account_holder}, now your balance is {self.balance}")
#         else:
#             print("You cannot deposit less than 0")
#
#     def check_balance(self):
#         print(f"You have {self.balance} left")
#
#     def print_account_details(self):
#         print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}")
#
# first_account = BankAccount (
#     account_number="1",
#     account_holder="Oleg",
#     balance=100
# )
#
# first_account.withdraw(amount=50)
# first_account.deposit(amount=100)
# first_account.check_balance()
# first_account.print_account_details()