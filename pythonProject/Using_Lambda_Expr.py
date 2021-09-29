def square(num):
    return num**2


num_list = [1, 2, 3, 4, 5]
# print(map(square, num_list)) # will show the memory location
# To access the output use the for loop: Method-1
for item in map(square, num_list):
    print(item)
# If we want the result in a list format we have to type cast: Method-2
print(list(map(square, num_list)))


def even_check(num1):
    return num1 % 2 == 0


# filter built in function is used if argument fun returns True/False values
# print(filter(even_check,num_list)) # will show the memory location
# Method-1
for j in filter(even_check, num_list):
    print(j)
# Method-2
print(list(filter(even_check, num_list)))
print(list(map(even_check, num_list)))
print(list(filter(square, num_list)))


# LAMBDA EXPRESSION FOR THE ABOVE FUNCTIONS
print(list(map(lambda x: x**2, num_list)))
print(list(filter(lambda y: y % 2 == 0, num_list)))
