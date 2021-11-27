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
