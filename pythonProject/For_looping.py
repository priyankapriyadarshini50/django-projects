import time


# This program shows number 0 to 10
def different_format():
    for i in range(10):
        print(i)
    print("End of program")

    # the following shows the step count
    for n in range(1, 5):
        print(n)
    print("This is the end of the loop")
    # get only the even numbers up to 20
    for p in range(2, 20, 2):
        print(p)
    print("---END---")
    # get the odd numbers up to 20
    for q in range(1, 20, 2):
        print(q)
    print("This is end!")
    # direct using the sequence
    for r in [1, 2, 3, 4, 5]:
        print("The value is {0}".format(r))
    print("{0:_^13}".format('END'))


def power_of_two():
    power = 1
    for expo in range(16):
        print("2 to the power of", expo, "is:", power)
        power *= 2


def count_for_hide_and_seek():
    for i in range(1,6):
        print(i,"Mississippi")
        time.sleep(1)
    print("Ready or not, here I come!")


def enter_secret_word():
    while True:
        exit_word = input("Enter the exit word:")
        if exit_word == "chupacabra":
            break
    print("You have successfully left the loop.")


# This function eats the vowel letters and prints uneaten letters
def remove_vowels():
    user_word = input("Enter a word:").upper()
    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            print(letter)


# This function creates words without vowels
def create_word_without_vowels():
    word_without_vowels = ""
    user_word = input("Enter a word:").upper()
    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            word_without_vowels += letter
    print("The word without vowels is:", word_without_vowels)


def remove_vowels_from_word(word_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = []
    for word in word_list:
        for letter in word:
            if letter in vowels:
                word = word.replace(letter, '')
        new_list.append(word)
    return new_list


words = ['cat', 'ink', 'egg', 'soap', 'queen']
print(remove_vowels_from_word(words))



def test_exe3():
    word = ""
    for ch in "john.smith@pythoninstitute.org":
        if ch == "@":
            break
        else:
            word += ch
    print(word)


def test_exe4():
    for digit in "0165031806510":
        if digit == "0":
            print("x",end="")
            continue
        print(digit, end="")


# Using for loop with else statement(check if the list contains even numbers)
def check_even_num(my_list):
    for elem in my_list:
        if elem % 2 == 0:
            print('The list contains a even number.')
            break
    else:
        print('There is no even number in the list')


print("List 1:")
check_even_num([1, 3, 5])
print("List 2:")
check_even_num([1, 5, 4, 10])
# different_format()
# power_of_two()
# count_for_hide_and_seek()
# enter_secret_word()
# remove_vowels()
# create_word_without_vowels()
# test_exe3()
# test_exe4()


