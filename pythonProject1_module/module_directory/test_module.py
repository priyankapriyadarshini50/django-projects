print("I like to be a module")
print(__name__)
"""test_module.py is an example of python module"""
__counter = 0


def suml(my_list):
    global __counter
    sum = 0
    for elem in my_list:
        sum += elem
        __counter += 1
    return sum


def prodl(my_list):
    global __counter
    prod = 1
    for elem in my_list:
        prod *= elem
        __counter += 1
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but i can do some tests for you")
    test_list = [i + 1 for i in range(5)]
    print(suml(test_list) == 15)
    print(prodl(test_list) == 120)
    print(__counter)
else:
    print("I am an import module! ")
