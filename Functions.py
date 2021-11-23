"""
#simple function
def greet_user(name): #name is a parameter
    print("Hello " + name.title()+'!')

greet_user('dan') #'dan' is an argument

#positional arguments
def describe_farm(farmowner,farmtype,farmsize):
    print(farmowner + ' owns a ' + farmtype + ' and the farm is ' + str(farmsize) + ' acres!')

describe_farm('John','asparagus',50)

#Keyword Arguments
def describe_farm(farmowner,farmtype,farmsize):
    print(farmowner + ' owns a ' + farmtype + ' and the farm is ' + str(farmsize) + ' acres!')

describe_farm(farmowner = 'John',farmtype = 'asparagus',farmsize = 50) #an example of keyword arguments

#default values
def describe_farm(farmowner,farmsize,farmtype = 'Cattle'): #'Cattle' is the default type for farm type
    print(farmowner + ' owns a ' + farmtype + ' farm and the farm is ' + str(farmsize) + ' acres!')

describe_farm(farmowner='Jeff',farmsize=50)

#8-3 T-shirt
def make_shirt(size = 'medium',text = 'Happy face'):
    print("Your shirt size is " + size + ' and your message on your shirt says: ' + text)
make_shirt()
make_shirt(size='large',text='hola mundo')

#make an argument optional
#set a default value for a parameter
#ex. making the middle name optional

def fullname(first,last,middle=''):
    if middle:
        name = first + ' ' + middle + " " + last
    else:
        name = first + ' ' + last
    return name.title()

print(fullname('daniel','gauerke'))
print(fullname('daniel','gauerke','charles'))

#storing a dictionary in a function
def build_person(first,last,age=''):
    person = {'first':first, 'last':last}
    if  age:
        person['age'] = age
    return person
musician = build_person('johnny','winter',age='death')
print(musician)

def get_formatted_name(first,last):
    fullname = first+' '+last
    return fullname.title()

while True:
    print('\nPlease tell me your name: ')
    print("(enter 'q' at any time to quit)")

    fname = input('First name: ')
    if fname == 'q':
        break

    lname = input('Last name: ')
    if lname == 'q':
        break

    formatted_name = get_formatted_name(fname,lname)
    print('\nHello,' + formatted_name + '!')

"""
#Exercises

#8-6 City Names


"""
def city_country(city,country):
    message = "\""+city + ', ' + country+"\""
    return message.title()
print(city_country('Santiago','chile'))

#8-7 Album
def make_album(artist_name,album_title,num_of_tracks=''):
    album = {'Artist Name':artist_name,'Album Title':album_title}
    if num_of_tracks:
        album['Number of Tracks'] = num_of_tracks
    return album
album1 = make_album('Jimi Hendrix','Purple Haze')
album2 = make_album('George Strait','Here for a Good Time')
album3 = make_album('Keith Whitley','No Stranger to the Rain',num_of_tracks=12)
list = [album1,album2,album3]
for album in list:
    print(album)


while True:
    print("\nEnter album information")
    print("\nEnter 'q' to exit")

    artist_name = input("What is the artist's name? ")
    if artist_name == 'q':
        break

    album_name = input("What is the album's name? ")
    if album_name == 'q':
        break

    num_of_tracks = input("What is the number of tracks on the album? ")
    if num_of_tracks == 'q':
        break
    print(make_album(artist_name,album_name,num_of_tracks))
    break

"""
#Exercises
#8-9 Magicians

"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


#8-10 Great Magicians
def make_great(magicians):
    great_magicians = [] #establishing a placeholder list to place values into
    while magicians: #while there are still elements in the magicians list
        great_magician = magicians.pop() #removing the element and storing it
        great_magician += " the great"    #adding the great to the element
        great_magicians.append(great_magician)  #placing the new element inside the placeholder list
    for greatmagician in great_magicians:       #placing all the elements from the placeholder list to the original list
        magicians.append(greatmagician)
    return magicians
names = ['john','toby','honey','houdini','david copperfield']

#8-11 Unchanged Magicians

makegreate = make_great(names[:])
show_magicians(names)
show_magicians(makegreate)
show_magicians(names)

"""
#passing an arbitrary number of arguments

def make_pizza(*toppings): #the * tells python to make an empty tuple called toppings
    print("Estamos haciendo su pizza con los toppings: ")
    for topping in toppings:
        print("- "+topping)


make_pizza('queso','championes','pepperoni','aceitunas','pimenton')
