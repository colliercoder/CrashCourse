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

#Continiued

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
        break
    else:
        print("I will add " + pizza_toppings + " to the pizza")
        toppings.append(pizza_toppings)

print("Your pizza has",end = ' ')
for topping in toppings:
    print(topping, end = ' ')
print('on it.')

"""
#While loop with lists and dictionaries
#moving items from one list to another
"""
unconfirmed_users = ['dakota','dallas','givi']
confirmed_users = []

while unconfirmed_users: #runs as long as unconfirmed_users list is not empty
    current_user = unconfirmed_users.pop() #removing one at a time from the end of the list

    print("Verifiying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instances of specific values from a list

pets = ['cat','dog','cat','cat','fish','fish','dog','ferret']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling a dictionary with user input

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary:
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    
"""

#7-8 Deli and 7-9 Pastrami

sandwich_orders = ['turkey club','ham and swiss','roastbeef and mustard','reuben','pastrami','pastrami','pastrami']
finished_sandwiches = []
print("Dan's Deli has ran out of pastrami for today...")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders: #runs as long as sandwich_orders list is not empty
    complete_sandwich = sandwich_orders.pop()
    print('I will make your ' + complete_sandwich + ' now!')
    finished_sandwiches.append(complete_sandwich)

for sandwich in finished_sandwiches:
    print('Your ' + sandwich + ' has been made!')
print('The following sandwiches have been made: ')
for sandwich in finished_sandwiches:
    print(sandwich.title(), end = ', ')

#7-10 Dream Vacation:
responses = {}

polling_active = True
while polling_active:
    #prompting the user
    prompt = '\nWhat is your dream vacation?'
    prompt += '\nAnswer: '

    vacation = input(prompt)

    prompt2 = '\nWhat is your name? '
    name = input(prompt2)
    #storing the responses in the dictionary
    responses[name] = vacation

    repeat = input('Would you like to let another person answer? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\nPolling is complete...')
print('\nPoll Results')
for name, response in responses.items():
    print(name.title()+ " would like to go to " + response.title() + " on their dream vacation!")


