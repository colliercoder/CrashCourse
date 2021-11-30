filename = 'guest_book.txt'

while True:
    name = input("What is your name? Type 'end' to end program \n\n")
    if name == 'end':
        break
    else:
        welcome_name = 'Welcome ' + name.title()
        with open(filename,'a') as file_object:
            file_object.write(welcome_name.title() + '\n')