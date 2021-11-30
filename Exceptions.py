#Exceptions

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input("\nSecond number: ")
    if second == 'q':
        break
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        print(answer)

#Illustrating file not found error

filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry the file ' + filename + ' does not exist.'
    print(msg)