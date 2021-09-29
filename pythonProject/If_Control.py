# This is a program displays the greeting messages according to time
def greeting_msg():
    time = float(input("What is the time in hh.mm format: "))
    if time == 12.00:
        print("This is noon")
    elif time > 21.00:
        print("This is night, Goodnight!")
    elif time > 17.00:
        print("This is evening, Good evening!")
    elif time > 12.00:
        print("This is afternoon, Good afternoon!")
    else:
        print("This is morning, Good morning!")


# This function finds the largest of three numbers
def find_largest_number():
    # read the three numbers
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    number3 = int(input("Enter the third number:"))
    # assign number1 value as the largest number
    # largest_number = number1
    # if number2 > largest_number:
    #   largest_number = number2
    # if number3 > largest_number:
    #    largest_number = number3
    # print("The largest number is:", largest_number)
    # check the largest of the three numbers
    # pass the value to largest_number variable
    largest_number = max(number1, number2, number3)
    print("The largest number is:", largest_number)


def find_plant():
    plant_name = input("Enter the name of the plant:")
    if plant_name == "Spathiphyllum":
        print("Yes, Spathiphyllum is the best plant ever!")
    elif plant_name == "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
    else:
        print("Spathiphyllum! Not " + plant_name + "!")


# This function calculate the tax amount of the citizens
def tax_calculator():
    income = float(input("Please, Enter your income amount:"))
    if income < 85528.0:
        tax = income * 0.18 - 556.2
        if tax > 0:
            tax = tax
        else:
            print("The tax is: 0.0 thaler")
            exit()
    else:
        tax = 14839.2 + (income - 85528) * 0.32
    tax = round(tax, 0)
    print("The tax is:", tax, "thaler")


# This function defines whether the entered year is a leap or common year
def find_leap_common_year():
    year = int(input("Enter a year: "))
    if year > 1582:
        if year % 4 != 0:
            print("It's a common year")
        elif year % 100 != 0:
            print("It's a leap year")
        elif year % 400 != 0:
            print("It's a common year")
        else:
            print("It's a leap year")
    else:
        print("Not within the Gregorian calendar period")


greeting_msg()
find_largest_number()
find_plant()
tax_calculator()
find_leap_common_year()
