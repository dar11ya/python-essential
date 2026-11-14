"""Course plan:
1. Introduction to OOP: an overview of classes
2. Inheritance
3. Encapsulation
4. Polymorphism
5. Abstraction
6. Working with recursion
7. Data structures
8. Python modules
9. Reading and writing files
10. Programming paradigms and code style standards"""

# Introduction to OOP: an overview of classes
"""Everything around us is an object. Different objects can be grouped into categories. For example, there is a class of
flying machines that includes many kinds of aircraft. Among them are different types of airplanes, for example
single-engine and twin-engine ones. Among all airplanes we can single out the class of passenger planes. All passenger planes
are aircraft, but not all aircraft are passenger planes."""

"""There are material and non-material objects. Non-material ones include music, songs, processes and ideas, movies and videos. We can
also sort non-material objects into categories. There are many music genres. Music can be created with notes, to
be played at concerts, or with software, to store and play it back. The same goes for
material objects: we can draw blueprints of them, which helps us understand which parts are needed
and how to combine them to build the object. So building a plane happens step by step. First comes the blueprint, then materials are
gathered and assembled, and that is how a plane is made. Moreover, one blueprint can be used to build many different planes. """

"""In OOP, the blueprint is a class, and the final result that gets created is an object/instance of the class."""

"""A class and an instance are non-material, and they are stored in the computer's RAM."""

"""A plane has the following properties: side text, a main color, additional colors, number of side doors - 5, and a pilot,
which means it is not autopiloted. Let's try to create it as an object of a class"""
"""__init__ is the class constructor. It specifies which properties an instance created from the
class will have. Functions defined with def inside a class are called methods, not functions!"""

"""The first argument is self. It lets us refer to the instance itself while it is being built"""

# class Plane:
#     def __init__(
#             self,
#             side_text,
#             main_color,
#             additional_colors,
#             side_doors_colors,
#             autopilot
#     ):
#         self.side_text = side_text # Creates the side_text property, which is available once an instance is created
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

"""If we try to call Plane.side_text, it will raise an Error"""

# airbus = Plane(
#     side_text="Delta",
#     main_color="white",
#     additional_colors=["red", "blue"],
#     side_doors_colors=4,
#     autopilot=False
# )

# print(f"Additional colors: {airbus.additional_colors}")

"""A plane can take off and land. These behaviors can be described with instance methods of the class."""
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
#     def take_off(self):  # Added an instance method for taking off
#         print(f"{self.side_text} takes off")
#
#     def land(self): # Added an instance method for landing
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

"""Some properties can be shared by all planes and be defined in advance by the blueprint, for example the engine type.
Example: Engine type: turbofan"""

# class Plane:
#     engine_type = "Turbofan" # This is a class attribute. It applies to all instances.
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
#     def take_off(self):  # Added an instance method for taking off
#         print(f"{self.side_text} takes off")
#
#     def land(self): # Added an instance method for landing
#         print(f"{self.side_text} lands")
#
# print(f"Type: {Plane.engine_type}")

"""CLASS METHODS"""
"""To mark a method as a class method rather than an instance method, we use the special @classmethod decorator, which adds new behavior.
In our case, the first argument is not self but the class itself"""
"""Class methods can be called directly on the class"""

# class Plane:
#     engine_type = "Turbofan" # This is a class attribute. It applies to all instances.
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

# STATIC METHODS
"""Can be called both on the class and on an instance of the class"""
"""Suppose we want to calculate fuel consumption for a given distance.
Consumption per 1000 km of flight:
-The plane burns 7 tons of fuel per hour
-At cruising speed it covers 900 km per hour
-For 1000 km the plane uses (7000 x 1000) / 900 = ~7778 kg of fuel"""

# class Plane:
#     engine_type = "Turbofan" # This is a class attribute. It applies to all instances.
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
Task: Developing a class for managing orders
Create an Order class that models an order in an online store. The class must have the
following attributes and methods:
• Class attributes:
• order_id (integer) - unique order identifier.
• customer_name (string) - name of the customer placing the order.
• items (list of strings) - list of items in the order.
• Class methods:
• __init__(self, order_id, customer_name): Class constructor that takes order_id and
customer_name and initializes the attributes.
• add_item(self, item): Adds an item to the items list.
• remove_item(self, item): Removes the given item from the items list if it is
present.
• print_order_details(self): Prints the order details, including order_id,
customer_name and the list of items.
• Tasks to complete:
• Create an object of the Order class with any order_id and customer_name.
• Add a few items to the order using the add_item method.
• Remove one or more items using the remove_item method.
• Print the order details using the print_order_details method.
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
Implementing a class for managing books in a library
Create a Book class with the attributes title, author, genre and status (available/unavailable). Add
methods for borrowing a book (borrow_book()), returning a book (return_book()) and printing
book information (print_details()).
"""

# class Book:
#     def __init__(self, title, author, genre, status):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.status = status
#
#     def borrow_book(self):
#         if self.status == "available":
#             print(f"You borrowed {self.title}")
#             self.status = "unavailable"
#         else:
#             print("This book is unavailable")
#
#     def return_book(self):
#         self.status = "available"
#
#     def print_details(self):
#         print(f"The book called {self.title} by {self.author} is {self.genre} and is {self.status}")
#
# book1 = Book(
#     title="1984",
#     author="George Orwell",
#     genre="Dystopian fiction",
#     status="available"
# )
#
# book1.borrow_book()
# book1.return_book()
# book1.print_details()

"""Implementing a class for managing a bank account
Create a BankAccount class with the attributes account_number, account_holder, balance. Implement
methods for withdrawing funds (withdraw()), depositing funds (deposit()), checking the balance
(check_balance()) and printing account information (print_account_details())."""

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
