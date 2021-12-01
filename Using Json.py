#Using json.dump() and json.load()
#Json stands for javascript object notation

import json
"""
numbers = [x for x in range(1,11)]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename,'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)

username = input("What is your name? ")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, " + username + "!")

def greet_user():
    #Greet the user by name.
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user()

#Refractoring: the process of taking a function with a lot of code and portioning it into different functions
"""
def get_stored_username():
    #Get stored username if available
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    #Prompt for a new username.
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()

    question = input("Is your username " + username + "?")
    if question == 'yes':
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()

    print("We'll remember you when you come back, " + username + "!")

greet_user()



