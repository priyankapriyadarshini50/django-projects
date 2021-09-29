# This function asks user to guess the correct number
def guess_the_number():
    number = 26
    running = True
    while running:
        guess = int(input('Guess a number or type False to stop:'))
        if guess == number:
            print("You have guessed it correct, Congratulations!")
            running = False
        elif guess > number:
            print("You have guessed a higher number.")
        else:
            print("You have guessed a lower number.")
    print("The while loop is closed")


# exit the loop when i is 3
def annonymous():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
        if i == 3:
            break
        else:
            print('The number {0}'.format(i)) # when break executed no other else statement executed
    print('Exit the while loop')
# the same above program using for loop exit the loop when i is 5
    for i in range(0,10):
        print(i)
        if i == 5:
            print('The loop breaks here')
            break


def find_largest():
    largest_number = -999999
    number = int(input("Enter a number or type -1 to stop:"))
    while number != -1:
        if number > largest_number:
            largest_number = number
        number = int(input("Enter a number or type -1 to stop:"))
    print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
def even_odd_counter():
    number = int(input("Enter a number or type 0 to stop:"))
    even_number_counter = 0
    odd_number_counter = 0
    while number:
        if number % 2 == 0:
            even_number_counter += 1
        else:
            odd_number_counter += 1
        number = int(input("Enter a number or type 0 to stop:"))
    print("We have entered",even_number_counter, "even numbers and", odd_number_counter, "odd numbers")


def guess_secret_number():
    secret_number = 777
    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    guess_number = int(input("Enter an integer number or type 0 to stop:"))
    while guess_number != 0:
        if guess_number == secret_number:
            print("Well done, muggle! You are free now.")
            exit()
        else:
            print("Ha ha!, You are stuck in my loop!")
            guess_number = int(input("Enter an integer number or type 0 to stop:"))


def lothar_hypothesis():
    c0 = int(input("Enter a non-negative integer and type 0 to stop:"))
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            print("even number")
            c0 = c0 // 2
        else:
            print("odd number")
            c0 = 3 * c0 + 1
        print(c0)
        steps += 1
    print("The total number of iteration required to reach number 1 is:", steps)


#guess_the_number()
#annonymous()
#find_largest()
#even_odd_counter()
#guess_secret_number()
lothar_hypothesis()
