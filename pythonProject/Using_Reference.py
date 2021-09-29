shoppinglist = ['apple', 'orange', 'cherry', 'pear']
mylist = shoppinglist
print("The items in the shopping list are %s" % shoppinglist)
print("The items in mylist are %s" % mylist)
# delete one item from the shopping list
del shoppinglist[0]
print("Now the items in the shopping list are %s" % shoppinglist)
print("Now the items in mylist are %s" % mylist)
# make a copy of the list
mynewlist = shoppinglist.copy()
del mynewlist[-1]
print("The items in my new shopping list are %s" % mynewlist)
print("Now the items in the shopping list are %s" % shoppinglist)
