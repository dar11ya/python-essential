# ENCAPSULATION
# Consider a flat in an apartment building. The stairwell is a public place, so there is some information available
# to every visitor of the building. For example, the flat number, the meter readings if the meter is located
# outside, and the color of the door. At the same time, some information is not available. For example, the number of rooms,
# the interior design, whether there is a TV. But this information can be learned by, for example, our friends whom we invite
# into our flat. That way they can find out that the number of rooms is 3, the interior design is modern, and that
# there is a TV in the flat. This information is not available by default. However, even guests do not know
# every detail of the flat, for example whether there is a safe in the flat, what is kept in the safe, and what the flat is worth.
# Without the owners' permission, our guests cannot find out all the information. The fact that the flat has a safe should not
# affect how we talk with friends. We can still watch TV together. At the same time, the design of the flat or
# the presence of a TV should not affect the work of the inspectors who record the meter readings.
# A flat as an object exists independently of who interacts with it (guests, an inspector or the owners).

# A flat is an object created from a certain class (the blueprint of that flat). We define in advance the
# properties of the flat at the class level as attributes (flat number, presence of a TV) and methods (reading the
# meter, opening the safe). We also call any entity that interacts with an object
# or a class a client. In the case of a flat, the clients are the inspector, friends and owners.

"""Encapsulation is one of the core principles of OOP. It consists of bundling data (attributes)
and the methods that process them into a single unit (a class)
    - Hiding the internal implementation details from the client
    - Interacting through predefined methods"""

# Let's implement the Flat class

class Flat:
    def __init__(self, number):
        self.number = number
        self.door_color = "Brown"
        self.electricity_readings = 0

    def display_number(self):
        print(f"Flat number is {self.number}")

if __name__ == "__main__":
    flat = Flat(212)

    flat.display_number()  # This is a public method, available outside the class and in child classes
    print(f"Flat has {flat.door_color} door color")
    print(f"Electricity readings for flat {flat.number}: {flat.electricity_readings}")

# All the attributes we created here are public (flat number, meter readings, door color)
