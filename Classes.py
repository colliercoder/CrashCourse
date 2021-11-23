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