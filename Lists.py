#Good practice to make the names of your lists plural ie. letters,digits,names
#Square brackets [] indicate a list

countries = ['mexico','panama','honduras','canada','turkey','costa rica','australia','colombia']

message = "My first country I ever travelled to was " + countries[6].title() + "."

print(message)

motorcycles = ['honda','ducati','yamaha','harley davidson']

motorcycles[0]='suzuki'

print(motorcycles)

motorcycles.append('honda')

print(motorcycles)

motorcycles.append('vespa')
motorcycles.append('indian')

#can only append one item at a time

print(motorcycles)

motorcycles.insert(0,'vespa')
print(motorcycles)


#deleting items in a list
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)

motorcycles.append(popped_motorcycle)
print(motorcycles)
print("The last motorcycle that I owned was a " + popped_motorcycle.title() + '.')

first_owned = motorcycles.pop(0)
print("The first motorcyle that I owned was a " + first_owned.title() +'.')

#if you want to delete the item and not use it, use del
#if you want to delete the item from the list and use it. use pop

#if you want to remove an item from a list without knowing the index. use remove()
#remove() only deletes the first occurence of the value you specify


motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")

#Excercise 3-4
guest_list = ['Nicola Tesla','Isaac Newton','King of England','Alejandra','Steve Jobs','Mike Tyson']
for x in guest_list:
    print("Greetings "+ x+'!'+"\nYou are invited to the 3rd annual dinner hosted by me Daniel Gauerke")

print("\n\n")

#Exercise 3-5
unable = guest_list.pop(0)
print("It troubles me that "+unable+" cannot make it to the dinner tonight. ")
guest_list.insert(0,'Benjamin Franklin')
print("\n\nWith pleasure I am now inviting " + guest_list[0]+ " to the dinner.\n")
for x in guest_list:
    print("\nGreetings "+x+'!'+"\nYou are invited to the 3rd annual dinner hosted by yours truly, Daniel Gauerke")

#Exercise 3-6
print("Good news! I found a bigger dinner table so I will invited 3 new guests\n")
guest_list.append("Lourdes Amaya")
guest_list.insert(3,"Jacob Gauerke")
guest_list.insert(0,"Kelly Gauerke")

for x in guest_list:
    print("\nGreetings "+x+'!'+"\nYou are invited to the 3rd annual dinner hosted by yours truly, Daniel Gauerke")

#Exercise 3-7
print("Unfortunately guests I only can invite two people.")
while len(guest_list) > 2:
    uninvited = guest_list.pop(0)
    print("I'm sorry "+ uninvited+" ,but you are not invited to the dinner anymore")

for x in guest_list:
    print("\nGreetings "+x+'!'+"\nYou are still invited to the 3rd annual dinner hosted by yours truly, Daniel Gauerke")

del guest_list[0]
del guest_list[0]
print(guest_list)




