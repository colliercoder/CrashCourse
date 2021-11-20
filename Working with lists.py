#Exercise 4-1

pizzas = ['cheese','supreme','veggie','sausage']

for pizza in pizzas:
    print('I love '+pizza+' pizza!')
print("I really love pizza!")

for value in range(0,6):
    print(value)

#use range to make a list of numbers

numbers = list(range(1,10,3))
print(numbers)

squares=[]
for square in range(1,1000,2):
    squares.append(square**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehension

squares = [value**2 for value in range(1,10)]
print(squares)

#Exercise 4-3

for count in range(1,21):
    print(count)

#Exercise 4-4

# for count in range(1,1000001):
#     print(count)

#Exercise 4-5

# list = list(range(1,1000001))
# print(sum(list))
# print(min(list))
# print(max(list))

#Exercise 4-6

odd_list = list(range(1,21,2))
print(odd_list)

for number in odd_list:
    print(number)

#Exercise 4-7

threes = list(range(3,31,3))
for three in threes:
    print(three)

#Exercise 4-8/4-9
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

#Using a slice to copy a list
myfoods = ['brocoli','rice','chicken']
friendfoods = myfoods[:]
friendfoods.append('asparagus')
print(friendfoods)
