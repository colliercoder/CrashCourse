with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#keyword with closes the file once access to it is no longer needed
#.read() always returns a blank line at the end. use rstrip() to take it away
#put the r before the file path to convert to raw string
file_path = r"C:\Users\15402\PycharmProjects\CrashCourse\pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#making a list of lines from a file
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#creating a string holding the entirety of pi file
with open(file_path) as file_object: #first make a list of lines
    lines = file_object.readlines()
pi_string = '' #create an empty string
for line in lines: #loop through the created list
    pi_string += line.strip()   #add the lines line by line to the string pi_string
                                #.strip() needed to fit string on one line

print(pi_string)
print(len(pi_string))