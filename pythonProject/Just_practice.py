# This function prints the fullname of the user input name
def full_name():
    f_name = input("May I know your first name, please? ")
    l_name = input("May I know your last name, please? ")
    print("Thank You!", end=" ")
    print("Your full name is " + f_name + " " + l_name)
    print(f_name + " " + l_name)


# This function creates a rectangle using replication feature of string
def print_rectangle():
    print("+" + 10 * "-" + "+")
    print(("|" + " " * 10 + "|\n") * 5, end="")
    print("+" + 10 * "-" + "+")


# This function calculates the length of hypotenuse
def cal_hypotenuse():
    leg_a = float(input("Enter first leg length: "))
    leg_b = float(input("Enter second leg length: "))
    print("The Hypotenuse length is: " + str((leg_a ** 2 + leg_b ** 2) ** 0.5))


# This function do some arithmetic operations using type casting
def arithmetic_cal():
    var_a = float(input("Enter the first number: "))  # input a float value for variable a here
    var_b = float(input("Enter the second number: "))  # input a float value for variable b here
    print("The addition result is: ", (var_a + var_b))  # output the result of addition here
    print("The subtraction result is: " + str(var_a - var_b))  # output the result of subtraction here
    print("The multiplication result is: ", (var_a * var_b))  # output the result of multiplication here
    print("The division result is: " + str(var_a / var_b))  # output the result of division here

    print("\nThat's all, folks!")


full_name()
print_rectangle()
cal_hypotenuse()
arithmetic_cal()


