cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 5-6 Stages of Life:
age = input('What is the age')
age = int(age)
if age < 2:
    print('The person is a baby')
elif age <4:
    print('The person is a toddler')
elif age <13:
    print('The person is a kid')
elif age <20:
    print('The person is a teenager')
elif age < 65:
    print('The person is an adult')
else:
    print('The person is a senior')

#5-8 Hello Admin:

usernames = ['admin','john','cleo','reba','timmy']
usernames2 = ['admin','John','rob','rebeca','tim']
for name in usernames:
    if name.lower() in usernames2:
       print('pick another username')
    else:
       print(name+','+' is available')


