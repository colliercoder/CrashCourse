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

