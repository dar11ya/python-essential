""" Завдання1: Розробка класу для керування персоналом
Створіть систему класів, яка моделюватиме структуру персоналу в організації. Почніть зі
створення базового класу Employee, а потім розширте його для різних типів працівників.
Клас Employee
Атрибути екземпляру класу:
• name (рядок): Ім'я працівника.
• age (ціле число): Вік працівника.
• salary (число з плаваючою точкою): Заробітна плата працівника.
Методи класу:
• __init__(self, name, age, salary): Конструктор класу, який приймає name, age і salary та
ініціалізує відповідні атрибути.
• get_details(self): Повертає рядок із деталями працівника (ім'я, вік, заробітна плата).
Клас Manager (спадкоємець класу Employee)
Додаткові атрибути екземпляру класу:
• team (список об'єктів класу Employee): Список працівників, які підпорядковуються
менеджеру.
Додаткові методи:
• __init__(self, name, age, salary, team): Конструктор класу, який приймає додатково список
працівників для ініціалізації атрибута team.
• add_employee(self, employee): Додає працівника до списку team.
• remove_employee(self, employee): Видаляє працівника зі списку team.
• get_team_details(self): Виводить інформацію про всіх працівників у команді менеджера.
Завдання для виконання:
• Створіть об'єкт класу Employee з довільним іменем, віком і зарплатою.
• Створіть об'єкт класу Manager з довільним іменем, віком, зарплатою та порожнім
списком team
• Додайте декілька об'єктів класу Employee до команди менеджера за допомогою методу
add_employee.
• Видаліть одного працівника з команди менеджера за допомогою методу
remove_employee.
• Виведіть деталі менеджера та його команди за допомогою методів get_details та
get_team_details."""
# class Employee:
#     def __init__(self, name: str, age: int, salary: float):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#
#     def get_details(self):
#         return f"The employee called {self.name} has age {self.age} years old and gets salary {self.salary}."
#
# class Manager(Employee):
#     def __init__(self, name: str, age: int, salary: float, team: list[Employee]):
#         super().__init__(name, age, salary)
#         self.team = team
#
#     def add_employee(self, employee):
#         self.team.append(employee)
#
#     def remove_employee(self, employee):
#         if employee in self.team:
#             self.team.remove(employee)
#         else:
#             print("Employee is not in the team.")
#
#
#     def get_team_details(self):
#         if not self.team:
#             print("The team is empty.")
#         else:
#             for worker in self.team:
#                 print(worker.get_details())
#
# if __name__ == "__main__":
#     employee1 = Employee("Mark", 29, 43500)
#     employee2 = Employee("Bob", 34, 89000)
#     employee3 = Employee("Ruslan", 33, 6500)
#     print(employee1.get_details())
#
#     manager = Manager(name="Oleg", age=39, salary=80.3, team=[])
#     manager.add_employee(employee1)
#     manager.add_employee(employee2)
#     manager.add_employee(employee3)
#     manager.remove_employee(employee2)
#     manager.get_team_details()
#
#     manager2 = Manager(name="Maryna", age=21, salary=90, team=[])
#     manager2.get_team_details()
#     manager2.get_details()


"""Завдання 1: Реалізація класу для обробки геометричних фігур
Створіть клас Shape, який буде мати атрибут name (назва фігури) і метод area(), який повертатиме
площу фігури (за замовчуванням - 0). Створіть підкласи Rectangle і Circle, які успадковуватимуть
клас Shape і перевизначатимуть метод area() для обчислення площі прямокутника і кола
відповідно."""
#
# class Shape:
#
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         return 0
#
# class Rectangle(Shape):
#     def __init__(self, name, length, width):
#         super().__init__(name)
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return f"The area of these rectangle is {self.length * self.width}."
#
#
# class Circle(Shape):
#     PI = 3.14159
#
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#
#     def area(self):
#         return f"The area of these circle is {self.PI * self.radius**2}."
#
#
# if __name__ == "__main__":
#     circle_shape = Circle("", 10)
#     print(circle_shape.area())
#     rect1 = Rectangle("", 10, 20)
#     print(rect1.area())
#     any_shape = Shape("any_shape")
#     print(any_shape.area())

"""Завдання 2: Реалізація класу для обробки транспортних засобів
Створіть базовий клас Vehicle, який матиме атрибут speed (швидкість) і метод move(), який
виводить повідомлення про рух зі вказаною швидкістю. Створіть підкласи Car і Bicycle, які
успадковуватимуть клас Vehicle і перевизначатимуть метод move() для виведення
спеціалізованого повідомлення, відповідного до типу транспортного засобу.
Завдання для виконання:
• Створіть об'єкт класу Vehicle з довільною швидкістю і викличте метод move().
• Створіть об'єкт класу Car і перевизначте метод move() для виведення повідомлення:
"Автомобіль рухається зі швидкістю [speed] км/год".
• Створіть об'єкт класу Bicycle і перевизначте метод move() для виведення повідомлення:
"Велосипед рухається зі швидкістю [speed] км/год".
• Викличте методи move() для кожного з об'єктів."""

# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed

#     def move(self):
#         print(f"Транспортний засіб рухається зі швидкістю {self.speed} км/год")

# class Car(Vehicle):
#     def __init__(self, speed):
#         super().__init__(speed)

#     def move(self):
#         print(f"Автомобіль рухається зі швидкістю {self.speed} км/год.")

# class Bicycle(Vehicle):
#     def __init__(self, speed):
#         super().__init__(speed)

#     def move(self):
#         print(f"Велосипед рухається зі швидкістю {self.speed} км/год.")

# if __name__ == "__main__":
#     car = Car(speed=10)
#     bicycle = Bicycle(speed=20)
#     vehicle = Vehicle(speed=30)
#     car.move()
#     bicycle.move()
#     vehicle.move()
