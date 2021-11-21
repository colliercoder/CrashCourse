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
print('\n')
#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#changing the first 10 aliens to have different attributes
for alien in aliens[:10]:
    if alien['color']=='green':
        alien['color']= 'yelow'
        alien['points']=15
        alien['speed']='fast'
for alien in aliens[10:20]:
    if alien['color']=='green':
        alien['color']='orange'
        alien['points']=25
        alien['speed']='medium'
#Show the first 20 aliens:
for alien in aliens[:20]:
    print(alien)
print("...")

#Show how many aliens have been created
print('Total number of aliens: '+str(len(aliens)))

#lists nested in dictionaries looping through example

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#6-8 Pets

Jeff = {'name':'Jeff','animal type':'cat','owner name':'sheldon'}
Tim = {'name':'tim','animal type':'dog','owner name':'buster'}
Brian = {'name':'brian','animal type':'fish','owner name':'chucky'}

pets = [Jeff,Tim,Brian]

for pet in pets:
    print("\nThe pet's name is " + pet['name'].title())
    print("The pet's type is " + pet['animal type'].title())
    print("The pet's owner name is " + pet['owner name'].title())

#6-9 Favorite Places

favorite_places = {'John':['Chinatown, NY','China','Okinawa Japan'],
                   'Dan':['Oaxaca','Medellin','Germany'],
                   'Aleja':['Cartagena','Hungary','Africa']

}

for name,places in favorite_places.items():
    print(name+"'s favorite places are: ")
    for place in places:
        print(place,end=',')
    print('\n')

#6-11 Cities

cities = {'Brooklyn':{'country':'USA','population':300000,'Fact':'Brooklyn is in New York'},
          'Chinatown':{'country':'USA','population':200000,'Fact':'Chinatown is in New York'},
          'San Francisco':{'country':'USA','population':100000,'Fact':'San Francisco is a weird place'}

}

for city,cityinfo in cities.items():
    print(city+':')
    print(city+' is in the country of '+cityinfo['country']+'.')
    print('The population of ' + city +' is '+ str(cityinfo['population'])+'.')
    print('A fun fact about '+city+' is '+ cityinfo['Fact']+'.')
    print('\n')


