""" Task 1: Developing a class for managing staff
Create a system of classes that models the staff structure of an organization. Start by
creating a base class Employee, then extend it for different types of employees.
Employee class
Instance attributes:
• name (string): The employee's name.
• age (integer): The employee's age.
• salary (float): The employee's salary.
Class methods:
• __init__(self, name, age, salary): Class constructor that takes name, age and salary and
initializes the corresponding attributes.
• get_details(self): Returns a string with the employee's details (name, age, salary).
Manager class (inherits from Employee)
Additional instance attributes:
• team (list of Employee objects): The list of employees who report to the
manager.
Additional methods:
• __init__(self, name, age, salary, team): Class constructor that additionally takes a list of
employees to initialize the team attribute.
• add_employee(self, employee): Adds an employee to the team list.
• remove_employee(self, employee): Removes an employee from the team list.
• get_team_details(self): Prints information about all employees on the manager's team.
Tasks to complete:
• Create an Employee object with any name, age and salary.
• Create a Manager object with any name, age, salary and an empty
team list
• Add several Employee objects to the manager's team using the
add_employee method.
• Remove one employee from the manager's team using the
remove_employee method.
• Print the details of the manager and their team using the get_details and
get_team_details methods."""
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


"""Task 1: Implementing a class for handling geometric shapes
Create a Shape class with a name attribute (the shape's name) and an area() method that returns the
area of the shape (0 by default). Create subclasses Rectangle and Circle that inherit from
Shape and override the area() method to calculate the area of a rectangle and a circle
respectively."""
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
#         return f"The area of this rectangle is {self.length * self.width}."
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
#         return f"The area of this circle is {self.PI * self.radius**2}."
#
#
# if __name__ == "__main__":
#     circle_shape = Circle("", 10)
#     print(circle_shape.area())
#     rect1 = Rectangle("", 10, 20)
#     print(rect1.area())
#     any_shape = Shape("any_shape")
#     print(any_shape.area())

"""Task 2: Implementing a class for handling vehicles
Create a base class Vehicle with a speed attribute and a move() method that
prints a message about moving at the given speed. Create subclasses Car and Bicycle that
inherit from Vehicle and override the move() method to print a
specialized message matching the type of vehicle.
Tasks to complete:
• Create a Vehicle object with any speed and call the move() method.
• Create a Car object and override the move() method to print the message:
"The car is moving at [speed] km/h".
• Create a Bicycle object and override the move() method to print the message:
"The bicycle is moving at [speed] km/h".
• Call the move() method on each of the objects."""

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"The vehicle is moving at {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"The car is moving at {self.speed} km/h.")

class Bicycle(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"The bicycle is moving at {self.speed} km/h.")

if __name__ == "__main__":
    car = Car(speed=10)
    bicycle = Bicycle(speed=20)
    vehicle = Vehicle(speed=30)
    car.move()
    bicycle.move()
    vehicle.move()
