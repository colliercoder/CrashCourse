#reading the entire file and printing
with open('Exercise_10_1_LearningPython.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#looping through each line in the file and printing
file_path = r'C:\Users\15402\PycharmProjects\CrashCourse\Exercise_10_1_LearningPython.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#storing the lines as a list and looping through the list
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())