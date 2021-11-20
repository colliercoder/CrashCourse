#6-2 Favorite Numbers:
dict = {'dan':1,'jake':3,'alejandra':4}
for value in dict:
    print(value,dict[value])

#6-3 Glossary
glossary = {'variable':'stores information','list':'mutable and stores ints,floats,strings and other types','tuple':'an immutable list'}
for x in glossary:
    print(x.title() + ':'+glossary[x])
#another way pay attention to .items() and key,value
for key, value in glossary.items():
    print(key.title()+': '+value)
# Use the .keys() method to just print the keys
for key in glossary.keys():
    print(key.title())
# Use the .values() method to just print the values
print("the follwing definitions are: ")
for value in glossary.values():
    print(value)
#using the set() method you only get unique values
new_dict = {'User1':'Blue','User2':'Blue','User3':'Red'}
for value in set(new_dict.values()):
    #set() makes it only print 'Red' and 'Blue'
    print(value.title())

#6-5 Rivers
rivers = {'Nile':'Egypt','Congo':'DRC','Tigris':'Syria'}
for river,country in rivers.items():
    if country == 'Syria':
        print('The ' + river + ' river runs through the country of ' + country + ' I think?')
    else:
        print('The '+river+' river runs through the country of '+country+'.')
print('\n\nThe countries in this river dictionary are: ')
for country in rivers.values():
    print(country.title(),end=' ')
print('\n\nThe rivers in this river dictionary are: ')
for river in rivers.keys():
    print(river.title(),end=' ')

