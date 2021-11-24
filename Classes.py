
#making an object from a class is called instantiation
#you work with an instance of a class
class Dog(): #by convention capitalized names denote classes
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age atrributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self): #roll_over() is a method
        """Simulate rolling over in a response to a command"""
        print(self.name.title() + " rolled over!")
# a function that is a part of a class is called a method.
my_dog = Dog('Eli',13)
your_dog = Dog('Tunk',13)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + "years old.")

your_dog.sit()

#9-1 Restaurant
class Restaraunt():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaraunt(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaraunt." )
    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

chinese_restaurant = Restaraunt('Chinatown Buffet',"Chinese-American")
print(chinese_restaurant.restaurant_name.title(), chinese_restaurant.cuisine_type.title())

chinese_restaurant.describe_restaraunt()
chinese_restaurant.open_restaurant()

#9-2
italian_restaurant = Restaraunt('Emilios','Italian')
american_restaurant = Restaraunt('Burger King','American')
thai_restaurant = Restaraunt('Taste of Thai','Thai')

italian_restaurant.describe_restaraunt()
american_restaurant.describe_restaraunt()
thai_restaurant.describe_restaraunt()

#9-3 Users
class User():
    def __init__(self, username,password,age):
        self.username = username
        self.password = password
        self.age = age
    def describe_user(self):
        print("The username: "+self.username)
        print("The password: " + self.password)
        print("The user's age: " + str(self.age))
    def greet_user(self):
        print("Hello " + self.username + " and welcome back!")
user1 = User('danielg', 'password123', 24)
user2 = User('Jackatack21', 'teflondon123',16)
user3 = User('rebecablack', 'fridayfriyay', 14)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        #setting a default value for an attribute, notice how it is not in the __init__
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    #2 Modifying an attribute's value through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    #3 Incrementing an attribute's value through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading +=  miles
        else:
            print("You can't deduce miles from an odometer")

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''You can change an attributes value in three ways
1. change the value directly
2. set the value through a method
3. or increment the value'''

#1. change the value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#2 Modifying an attribute's value through a method (see above)
my_new_car.update_odometer(20)#plugging in 100 as the argument for the function update_odometer
my_new_car.update_odometer((15))
my_new_car.read_odometer()
#3Incrementing an attribute's value through a method (see above)
my_new_car.increment_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment_odometer(-1100)
my_new_car.read_odometer()

#9-4
class Restaraunt():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaraunt." )

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def set_number_served(self,served):
        if served >= self.number_served:
            self.number_served = served
            print(self.restaurant_name + " has served " + str(served) + " customers today!")
        else:
            print("You can't erase customers!...DUH!")

    def increment_number_served(self,more_customers):
        if more_customers >= 0:
            self.number_served += more_customers
            print(self.restaurant_name + " has served " + str(self.number_served) + " customers today!")
        else:
            print("You can't erase customers!...DOY")
            print(self.restaurant_name + " has served " + str(self.number_served) + " customers today!")

restaurant = Restaraunt('Kebab','Lebanonese')
restaurant.number_served = 20
print(restaurant.number_served)
restaurant.set_number_served(50)
restaurant.set_number_served(40)
restaurant.increment_number_served(20)
restaurant.increment_number_served(-20)

#9-5 Login Attempts
class User():
    def __init__(self, username,password,age):
        self.username = username
        self.password = password
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print("The username: "+self.username)
        print("The password: " + self.password)
        print("The user's age: " + str(self.age))
    def greet_user(self):
        print("Hello " + self.username + " and welcome back!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.username + " login attempts: " + str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.username + " login attempts are now set back to " + str(self.login_attempts))

user1 = User('danielg', 'password123', 24)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()


#Inheritance... Car is the parent class Parent class must be
#               part of the same file and come before the child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class with super (superclass = parent class)"""
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    #you can overrite methods from the parent class by giving a method in the child class with the same name
    #We didn't give the parent class a fill_gas_tank() method but if we did the following
    #would overwrite it.

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("Electric cars don't have gas tanks")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class with super (superclass = parent class)"""
        super().__init__(make,model,year)
        #
        self.battery = Battery()
my_tesla = ElectricCar('tesla','model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#9-6 Ice Cream Stand
class IceCreamStand(Restaraunt):
    def __init__(self, restaraunt_name, cuisine_type):
        super().__init__(restaraunt_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry','pistachio','hazelnut','cookies & cream']
    def display_flavors(self):
        print('The flavors are: ')
        for flavor in self.flavors:
            print("- " + flavor)
icecreamstand = IceCreamStand('I Scream for IceScream', 'Icecream')
icecreamstand.display_flavors()
"""
#9-7 Admin
class Admin(User):
    def __init__(self, username, password, age):
        super().__init__(username, password, age)
        self.privelages = ['can add post','can delete post','can ban user']
    def show_privelages(self):
        print("Here are the admin's privelages: ")
        for i, privelage in enumerate(self.privelages):
            print(str(i+1) + ' ' + privelage.title())
admin = Admin('daniel','asdf;lkj',24)
admin.show_privelages()
"""
#9-8
class Admin(User):
    def __init__(self, username, password, age):
        super().__init__(username, password, age)
        self.privileges = Privileges()

class Privileges():
    def __init__(self,privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are the admin's privelages: ")
        if self.privileges:
            for i, privilege in enumerate(self.privileges):
                print(str(i+1) + ' ' + privilege.title())
        else:
            print("This user has no privileges")



dan = Admin('daniel','asdf;lkj',24)
dan_privileges = [
    'can ban user',
    'can execute user',
    'can behead user',
    'just kidding...'
]
dan.privileges.show_privileges()
dan.privileges.privileges = dan_privileges

dan.privileges.show_privileges()

#9-9 Battery Upgrade
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
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class with super (superclass = parent class)"""
        super().__init__(make,model,year)
        #
        self.battery = Battery()
my_tesla = ElectricCar('tesla','model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

