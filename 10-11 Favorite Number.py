#10-11 Favorite Number:
import json

filename = 'favorite_numbers'
fav_number = input("What is your favorite number? ")
with open(filename,'w') as f_obj:
    json.dump(fav_number,f_obj)

with open(filename,'r') as f_obj:
    json.load(f_obj)

print("I know your favorite number. It's " + fav_number)

#10-12 Favorite Number Remembered
def favorite_number():
    filename = 'favorite_numbers'
    try:
        with open(filename, 'r') as f_obj:
            fav_number = json.load(f_obj)
    except FileNotFoundError:
        fav_number = input("What is your favorite number? ")
        with open(filename, 'w') as f_obj:
            json.dump(fav_number, f_obj)
    else:
        print("I know your favorite number. It's " + fav_number)

favorite_number()

