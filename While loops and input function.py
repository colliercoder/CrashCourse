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

