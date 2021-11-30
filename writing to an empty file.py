filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating and building.\n")

#appending to created file programming.txt using the append mode
with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datasets\n')
    file_object.write("I love creating apps that can run in a browser\n")



"""
open file in read only mode by default
'r' is read mode
'w' is write mode
'a' is append mode
'r+' is read and write mode

"""