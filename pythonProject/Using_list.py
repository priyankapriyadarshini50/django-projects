def list_operation():
    my_list = [2, 4, 5, 10, 6, 23]
    my_list.insert(1, 7)
    print(my_list)
    my_list.append(10)
    print(my_list)
    my_list[4] = 39
    print(my_list)
    print("the length of the list is:", len(my_list))


def list_sort():
    my_list = [8, 10, 6, 2, 4, 10]
    swapped = True
    while swapped:
        swapped = False  # no swaps so far
        for i in range(len(my_list) - 1):
            if my_list[i] < my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                print(i, my_list)
    # print(my_list)


def list_slicing():
    my_list = [10, 8, 6, 4, 2]
    new_list1 = my_list[1: 3]
    new_list2 = my_list[:3]
    new_list3 = my_list[3:len(my_list)]
    new_list4 = new_list2  # represents the same list and same memory location
    new_list2[2] = 3
    new_list5 = new_list1.copy()  # here copy or [:] copies the content and create two different list
    new_list1[0] = 11
    print(new_list1)
    print(new_list2)
    print(new_list3)
    print(new_list4)
    print(new_list5)


# This function finds the location of a given element(5) inside a list:
def find_location_elem():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(my_list)):
        if my_list[i] == 5:
            print("The number is found at index location", i)
            break
    else:
        print("The number is not in the list!")


# This function shows the number of hits for lucky number drawn
def lucky_num_drawn():
    number_chosen = [3, 7, 11, 42, 34, 49]
    number_drawn = [34, 11, 9, 42, 3, 49]
    hits = 0
    for number in number_chosen:
        if number in number_drawn:
            hits += 1
    print(hits)


# This function removes the repeated numbers from the list
def remove_repeated_num():
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    new_list = []

    for num in my_list:
        if num not in new_list:
            new_list.append(num)

    print("The list with unique elements only:")
    print(new_list)


def list_copying():
    list_1 = ["A", "B", "C"]
    list_2 = list_1
    list_3 = list_2
    del list_1[0]
    del list_2
    print(list_3)


# This function creates a list of squares of numbers
def square_list():
    squares = [i ** 2 for i in range(10)]
    print(squares)
    # create a list with the odd elements of square list
    odds = [x for x in squares if x % 2 != 0]
    print(odds)


def chessboard_setup():
    EMPTY = '-'
    board = []
  # board = [[EMPTY for i in range(8)] for j in range(8)]
    for i in range(8):
        row = [EMPTY for j in range(8)]
        if i == 1:
            row = ['PAWN' for j in range(8)]
        if i == 6:
            row = ['PAWN' for j in range(8)]
        board.append(row)

    board[0][0] = 'ROOK'
    board[0][7] = 'ROOK'
    board[7][0] = 'ROOK'
    board[7][7] = 'ROOK'

    board[0][1] = 'KNIGHT'
    board[0][6] = 'KNIGHT'
    board[7][1] = 'KNIGHT'
    board[7][6] = 'KNIGHT'

    board[0][2] = 'BISHOP'
    board[0][5] = 'BISHOP'
    board[7][2] = 'BISHOP'
    board[7][5] = 'BISHOP'

    board[0][3] = 'QUEEN'
    board[0][4] = 'KING'
    board[7][3] = 'QUEEN'
    board[7][4] = 'KING'
    print(board)


# This function do the hotel bookings (3 buildings, 15 floors and 20 rooms on each floor)
def hotel_booking():

    hotel = [[['False' for room in range(8)] for floor in range(6)] for building in range(3)]
    #  book a room 2nd building, 10th floor, room 14
    #hotel[1][9][13] = True
    hotel[0][2][3] = True
    print(hotel)


# This function convert numbers to letters usinf list comprehension
def numbers_to_letters():
    number_dictionary = {1:'a', 2:'b', 3: 'c', 4: 'd', 5: 'e'}
    letter_list = [number_dictionary[num_keys] for num_keys in number_dictionary.keys()]
    print(letter_list)


# This function removes vowels from the words using list comprehension
def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, '')
    return word


word_list = ['cat', 'hat', 'print', 'queen', 'shop', 'ink']
new_list = [remove_vowels(word) for word in word_list]
print(new_list)



# list_operation()
# list_sort()
# list_slicing()
# find_location_elem()
# lucky_num_drawn()
# remove_repeated_num()
# list_copying()
# square_list()
# chessboard_setup()
# hotel_booking()
numbers_to_letters()
