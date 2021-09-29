# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user
i = int(input("Enter an integer number:"))
if i % 4 == 0:
    print("This is a multiple of 4:", i)
elif i % 2 == 0:
    print("This is an even number", i)
else:
    print("This is an odd number:", i)
