def say(word, times=2):  # here times has a default argument value to 2
    print(word * times)


say('Priyanka', 5)  # calling the function using arguments
say('Hello')  # calling the function with one argument
s = "Hi"
y = 3
say(s, y)  # calling function through variables


def add(a, b=23, c=10):  # c is the default argument value
    """Prints the addition of three numbers"""
    x = a + b + c
    print('The addition value is', x)


add(5, 7)
#  add(b=10, c=3)  # This is a run time error as positional argument a is missing
add(a=15, b=7)  # here a and b are keyword arguments
#add()
add(5)
print(add.__doc__)


# usage of return statement
def maximum(m, n):
    """This function returns the maximum value.

    The two entered number can be decimal integers and the number of digits
    should be same such as 234 and 042."""
    if m > n:
        return m
    else:
        return n


o = input('Enter 1st number:')
p = input('Enter 2nd number:')
z = maximum(o, p)  # calling func with variables & maximum func return value assigned to z
print('The maximum number is:', z)
print(maximum.__doc__)
help(add)


# every functions return None value implicitly
def function():
    pass


print(function())


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_result = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    result = is_year_leap(yr)
    if result == test_result[i]:
        print("OK")
    else:
        print("FAIL")


# This function finds the prime numbers
def is_prime(num):
    if num > 1:
        divisor = 0
        for j in range(1, num + 1):
            if num % j == 0:
                divisor += 1

        if divisor > 2:
            return False

        else:
            return True


for i in range(1, 30):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# This program calculates the bmi
def lb_to_kg(lb):
    return lb * 0.45359237


def ft_and_inch_to_mtr(feet, inch=0):
    return feet * 0.3048 + inch * 0.0254


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:  # for long expression we can use backslash to continue the expression in a new line
        return None
    return weight / height ** 2


weight = lb_to_kg(176)
height = ft_and_inch_to_mtr(5, 7)
print(bmi(weight, height))


# This function checks whether three sides of given lengths can build a triangle.
def is_a_triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return None
    elif a + b > c and b + c > a and \
            c + a > b:
        return True
    else:
        print(" It can't be a triangle")
        return False


#print(is_a_triangle(3, 12, 14.5))
#print(is_a_triangle(1, -23, 0))
#print(is_a_triangle(0.23, 0.45, 0.32))


# This function checks if the triangle is a right angled triangle
def is_a_right_angle_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a > b and a > c:
            return a ** 2 == b ** 2 + c ** 2
        elif b > a and b > c:
            return b ** 2 == c ** 2 + a ** 2
        else:
            return c ** 2 == a ** 2 + b ** 2
    else:
        print("It can't be a right angle triangle")


print(is_a_right_angle_triangle(1, 3, 4))
#print('This is a right angle triangle:', is_a_right_angle_triangle(3, 4, 5))
#print('This is a right angle triangle:', is_a_right_angle_triangle(3, 12, 14.5))


# this function calculate the area of a triangle
def area_of_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        s = (a + b + c)/2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


print(area_of_triangle(3, 4, 6))


# This function find the factorials of given number
def factorial_function(n):
    if n > 0:
        facto_value = 1
        for i in range(1, n + 1):
            facto_value *= i
        return facto_value
    if n == 0:
        return 1


for i in range(0, 10):
    print(factorial_function(i))


def fibonacci_numbers(n):
    if n < 0:
        return
    elif n < 3:
        return 1

    fib_1 = fib_2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = fib_1 + fib_2
        fib_1, fib_2 = fib_2, sum
    return sum


for i in range(1,8):
    print(fibonacci_numbers(i))


# This function try to modify the list parameter inside the function
def operation_on_list(my_list):
    for i in range(len(my_list)):
        if my_list[i] == 3:
            del my_list[i]
    return my_list


print(operation_on_list([23, 54, 12, 3]))


# Checking for list arguments modification
def my_function(my_list_1):
    print("Print #1", my_list_1)
    print("Print #2", my_list_2)
    del my_list_1[0]
    print("Print #3", my_list_1)
    print("Print #4", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5", my_list_2)


# *ARGS RETURNS A TUPLE AND USER CAN AS MANY ARGUMENTS AS YOU WANT
def myfunc(*args):
    print(args)
    #return sum(args)


result = myfunc('priyanka')
print(result)


# **KWARGS RETURNS A DICTIONARY AND USER CAN PASS AS MANY AS KEYWORD ARGUMENTS THEY WANT
def my_fun(**kwargs):
    print(kwargs)
    for item in kwargs.keys():
        print(item)
        #print("The vegetable in the list:", kwargs['veggie'])


my_fun(fruit='apple', veggie='broccoli', diary='milk')


def myfunc_with_args(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[1], kwargs['animal']))


myfunc_with_args(1, 2, 30, 45, fruit='apple',animal='dog', food='egg')




