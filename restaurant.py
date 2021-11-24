"""Restaraunt class"""
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


"""Icecream Class"""
class IceCreamStand(Restaraunt):
    def __init__(self, restaraunt_name, cuisine_type):
        super().__init__(restaraunt_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry','pistachio','hazelnut','cookies & cream']
    def display_flavors(self):
        print('The flavors are: ')
        for flavor in self.flavors:
            print("- " + flavor)