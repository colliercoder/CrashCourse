cars = ['bmw','mercedes benz','toyota','ford','cheverlet','dodge','fiat','mclaren','bentley','rolls royce']
cars.sort()
print(cars)

#sorts the list in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

#sorted() function allows you to display the original list sorted without changing the actual order in the list

print(cars)
print(sorted(cars))

#reverse() reverses the order the list is currently in.

print(cars.reverse())

#len() returns the length of the list
print(len(cars))

#exercise 3-8
worldplaces = ['germany','italy','spain','colombia','iceland','greece']
print(worldplaces)
print(sorted(worldplaces))
print(worldplaces)
print(sorted(worldplaces,reverse=True))
print(worldplaces)
worldplaces.reverse()
print(worldplaces)
worldplaces.reverse()
print(worldplaces)
worldplaces.sort()
print(worldplaces)
worldplaces.sort(reverse=True)
print(worldplaces)