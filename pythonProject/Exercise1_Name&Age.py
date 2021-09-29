# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them which year that they will turn 100 years old.
name = input('Please enter your name:')
age = input("Please enter your age:")
age = int(age)
print("Your name is {0} and age is {1}".format(name, age))
turn = 2021 + (100 - age)
print("You will turn 100 on the year {0}".format(turn))
# asking the user for another number and printing out that many copies of the previous message.
num = input("Enter a integer:")
num = int(num)
for i in range(num):
    print("You will turn 100 on the year {0}".format(turn))
else:
    print("Iteration has completed")
