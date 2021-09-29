# This script shows the usage of tuple
myTuple = ("apple", "banana", "cherry", "melon", "mango", "grapes", "kiwi")
print("The number of items in myTuple:", len(myTuple))

#  Tuple with one item
Tuple1 = ("rose")  # contains string value
Tuple2 = ("orange",)  # This is the right way to write a tuple with one item
print('The data type of tuple1 is:', type(Tuple1))
print('The data type of Tuple2 is:', type(Tuple2))
Tuple3 = ("apple", 35, True, 67, False)
print('The length of the Tuple3 is:', len(Tuple3))
print('The data type of the Tuple3 is:', type(Tuple3))
# print the 2nd item of my Tuple
print('The 2nd item of myTuple is:', myTuple[1])
print('The last item of myTuple is:', myTuple[-1])
print("The 2nd item to 5th items are:", myTuple[1:6])
print('The last two items of myTuple are:', myTuple[-2:])
print('The last two items of myTuple are:', myTuple[5:])


def check_item():
    for i in range(len(myTuple)):
        print("This item is available in the tuple:", myTuple[i])


check_item()
y = list(myTuple)
y.append('papaya')
print("the list of items:", y)
myTuple = tuple(y)
print('The new changed tuple is:', myTuple)

# The zoo program
zoo = ('Monkey', 'Tiger', 'Deer')
print("The number of animals in the zoo is:", len(zoo))
new_Zoo = ('Elephant', 'Zebra', zoo)
print("The number of cages in the new zoo is:", len(new_Zoo))
print("All the animals in the new zoo are:", new_Zoo)
print("all the animals from the old zoo are:", new_Zoo[2])
print("The last animal brought from old zoo is:", new_Zoo[2][2])
name = 'Adya'
age = 4
print("%s is %s years old kid." % (name, age))  # in both places we can keep %s
print("The age is %d." % age)
# tuple join
Tuple4 = myTuple + Tuple2
print("The Tuple join result is:", Tuple4)
print('The length of the new Tuple is:', len(Tuple4))
# tuple multiplication
t1 = zoo * 3
print(t1)
print('Monkey' in zoo)
print("lion" not in zoo)


# RETURNS all THE ITEMS IN THE LIST OF TUPLES
def unpacking_tuple(list1):
    for name, b, c in list1:
        print(name, c)
        print(b)


unpacking_tuple([('Adya', 1, 2), ('Priyanka', 4, 5), ('Umesh', 8, 9)])


# RETURNS THE EMPLOYEE NAME WITH MAXIMUM HOURS OF WORKING
def check_employee(emp_list):
    working_hours = 0
    emp_name = ''
    for name, hours in emp_list:
        if hours > working_hours:
            working_hours = hours
            emp_name = name
    return emp_name, working_hours


result1, result2 = check_employee([('Tom', 800), ('Rashi', 300), ('Jim', 600), ('Todd', 200)])
print("The employee of the month is", result1, 'and working hours is', result2)
