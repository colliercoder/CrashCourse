#10-8 Cats and Dogs:
file_cat = 'cats.txt'
file_dog = 'dog.txt'

with open(file_dog,'w') as dog:
    dog.write('Popular Dog Names: \n')
    dog.write('Henry\n')
    dog.write('Buster\n')
    dog.write('Clyde\n')

"""
with open(file_cat,'w') as cat:
    cat.write("Popular Cat Names: \n")
    cat.write('Felix\n')
    cat.write('Chester\n')
    cat.write('Poophead\n')
"""
try:
    with open(file_dog,'r') as dog:
        for line in dog:
            print(line.strip())

    with open(file_cat,'r') as cat:
        for line in cat:
            print(line.strip())
except FileNotFoundError:
    pass