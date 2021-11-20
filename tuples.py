#tuple is a list that cannto be changed. immutable list is called a tuple
#you can overwrite a tuple but you cannot add or modify the tuple.

dimensions = (3,2)
print('Original Dimensions: ')
for dim in dimensions:
    print(dim)
dimensions = (4,3)
print('Modified Dimensions: ')
for dim in dimensions:
    print(dim)

buffet_items = ('rice','beans','chicken','brocoli','potatoes')
for food in buffet_items:
    print(food)
buffet_items = ('rice','beans','chicken','brocoli','potatoes','steak','butter')
for food in buffet_items:
    print(food)