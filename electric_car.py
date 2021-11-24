
"""A class that can be used to represent a battery in electric cars"""

from car import Car

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 300
        elif self.battery_size == 85:
            range = 350
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size == 85:
            print("No need to upgrade")
        else:
            self.battery_size = 85
            print("Your battery is now upgraded to " + str(self.battery_size))

"""A class that can be used to represent an Electric Car"""
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class with super (superclass = parent class)"""
        super().__init__(make,model,year)
        #
        self.battery = Battery()