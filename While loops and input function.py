"""
#Creating a multiple line input
prompt ='If you tell us who you are we can personalize the message for you.'
prompt+='\nWhat is your first name? '

name = input(prompt)
print('\nHello '+name.title()+'!')

#7-3 Multiples of Ten
prompt = "Is it a multiple of 3 game."
prompt += '\nEnter a number: '
number = input(prompt)
number =int(number)

if number % 3 == 0:
    print('The number ' + str(number) +' is divisible by 3.')
else:
    print('The number ' + str(number) + ' is not divisible by 3.')

#while loop example
current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1

prompt = "\n Tell me something and I will repeat it back to you"
prompt += "\n Enter 'quit' to end the program. "

#necessary to store an empty string in the message variable so python has somthing to check
#when it runs the while loop
message = ''
while message != 'quit':
    message = input(prompt)

    if message !='quit':
        print(message)

#implementing a flag. A flag is used when many conditions can cause the program to end. it simplififes the code.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

"""

#Using break
prompt = '\nTell me what city you would like to visit'
prompt += "\n Enter 'quit' when you are finished "

# while True: will run forever unless it reaches a break statement
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

#Using a continue statement
current_number = 0
while current_number < 100:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#7-4 Pizza Toppings
print("\n Hello welcome to Dan's Pizza Joint, home of the world's best pizza!")
prompt = "\n Please tell me what you would like on your pizza, "
prompt += "\n Enter 'done' when you are finished "

toppings = []
active = True
while active:
    pizza_toppings = input(prompt)

    if pizza_toppings == 'done':
        active = False
    else:
        print("I will add " + pizza_toppings + " to the pizza")
        toppings.append(pizza_toppings)

print("Your pizza has",end = ' ')
for topping in toppings:
    print(topping, end = ' ')
print('on it.')


