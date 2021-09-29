
shoplist = ['apple', 'banana', 'milk', 'eggs', 'sugar']


def shopping_list():
    """Displays the list of items, contained in the shopping list"""
    for i in shoplist:
        print("The shopping list contains:", i)
    print("The number of items in the shopping list: ", len(shoplist))


def add_item():
    """Add a new item to the shopping list and returns the length of the list"""
    shoplist.append('rice')
    print("Now the shopping list is:", shoplist)
    print("Now the number of items in the shopping list has changed to:", len(shoplist))


def sort_list():
    """Returns the shorted items of shopping list """
    shoplist.sort()
    print("sorted shopping list is:", shoplist)


def remove_item():
    """Deletes the items which are already purchased"""
    shoplist_full = True
    while shoplist_full:
        if shoplist == []:
            shoplist_full = False
            print("The shopping list is empty.")
        else:
            print("I have bought the item:", shoplist[0])
            del shoplist[0]
            print("Now my shopping list is :", shoplist)


print(shopping_list.__doc__)
shopping_list()
print(add_item.__doc__)
add_item()
print(sort_list.__doc__)
sort_list()
print(remove_item.__doc__)
remove_item()
