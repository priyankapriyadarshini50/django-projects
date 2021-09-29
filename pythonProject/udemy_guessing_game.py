from random import shuffle
my_list = ['', 'O', '']


# RETURNS A SHUFFLE LIST
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


# RETURN THE USER GUESS
def user_guess():
    global guess
    guessing = True
    while guessing:
        guess = int(input("Enter a number: 0, 1 or 2: "))
        if guess in [0, 1, 2]:
            guessing = False
    return guess


# CHECKS THE GUESS WITH THE LIST
def check_guess(mixed_list1, guess_index1):
    if mixed_list1[guess_index1] == 'O':
        print("CORRECT")
    else:
        print("WRONG GUESS!")


# SHUFFLE THE LIST
mixed_list = shuffle_list(my_list)
# GUESS A NUMBER
guess_index = user_guess()
# CHECK THE USER GUESS
check_guess(mixed_list, guess_index)
print(my_list)
