age = 34
name = "Priyanka"
kid = 1
status = "Married"
print("My name is {0}". format(name), end=' ') # end= concanenate two print statements
print('My age is {0}'. format(age))
print("{0} is {1}".format(name, status))
print('{0} is {1} years old woman'. format(name, age))
print('{0} has {1} kid'.format(name, kid))
print("{0} is a {1} years woman and has {2} child".format(name, age, kid))
print("{} is a {} years woman and has {} child". format(name, age, kid))
print("{a} is a {b} years woman and has {c} child".format(a=name, b=age, c=kid))
print("{name} is a {age} years woman and has {kid} child".format(name=name, age=age, kid=kid))
print("{0} is a {1} years old woman and she is {2} and has {3} child".format(name, age, status, kid))
# shorter form of format() method
print(f'{name} is a {status} woman')
# decimal precision of 3
print('{0:.2f}'.format(1.0/3)) # .2f means 2 digits after decimal
print('{0:.3f}'.format(1/4)) # .3f means 3 digit after decimal point
print("{0:_^13}".format('Priya'))
