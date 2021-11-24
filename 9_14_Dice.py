from random import randint
class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        roll = randint(1,self.sides)
        print(roll)
    def roll_die_num_of_rolls(self,num_of_rolls):
        sum = 0
        for i,x in enumerate(range(num_of_rolls)):
            roll = randint(1,self.sides)
            sum += roll
        average = sum/num_of_rolls
        print("The average after rolling the " + str(self.sides) +
              " sided die " + str(num_of_rolls) + " times is " + str(average))
x_die = Die(20)
x_die.roll_die()
x_die.roll_die_num_of_rolls(2000)




