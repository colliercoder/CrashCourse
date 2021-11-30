#10-6 Addition

print("2 number addition")

first = input("Give me a number add: ")
second = input("Give me another number to add: ")

try:
    sum = int(first) + int(second)
    print("The total of the two numbers provided is: \n")
    print(sum)
except ValueError:
    print("Please enter in numbers")

#10-7 Addition Calculator

print("2 number addition")

while True:
    first = input("Give me a number add. Type 'q' to quit."
                  "\nNumber: ")
    if first == 'q':
        break
    second = input("Give me another number to add. Enter 'q' to quit"
                   "\nNumber: ")
    if second == 'q':
        break

    try:
        sum = int(first) + int(second)
        print("The total of the two numbers provided is: \n")
        print(sum)
    except ValueError:
        print("Please enter in numbers")