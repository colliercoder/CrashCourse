#10-3 Guest
filename = '10_3.txt'
guest_name = input("What is your name? \n\n")
with open(filename,'w') as file_object:
    file_object.write(guest_name)
