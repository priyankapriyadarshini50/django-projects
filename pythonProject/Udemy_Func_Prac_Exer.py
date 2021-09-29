# LESSER OF TWO EVENS
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # BOTH THE NUMBERS ARE EVEN
        return min(a, b)
    else:
        # ONE OR TWO NUMBERS ARE ODD
        return max(a, b)


# Check
print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


# ANIMAL CRACKERS
def animal_crackers(my_string):
    str_list = my_string.lower().split()
    # RETURNS A LIST OF WORDS WITH LOWER CASE
    print(str_list)
    return str_list[0][0] == str_list[1][0]


# Check
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY
def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


# check
print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# LEVEL 1 PROBLEMS
# OLD MCDONALD: ONE WAY Solution
def old_macdonald_sol1(name1):
    new_name = ''
    for i in range(len(name1)):
        if i == 0 or i == 3:
            new_name += name1[i].upper()
        else:
            new_name += name1[i]
    return new_name


# OLD MCDONALD: SECOND WAY Solution
def old_macdonald_sol2(name2):
    text1 = name2[0].upper()
    text2 = name2[1:3]
    text3 = name2[3].upper()
    text4 = name2[4:]
    return text1 + text2 + text3 + text4


# OLD MCDONALD: SECOND WAY Solution
def old_macdonald_sol3(name3):
    text1 = name3[:3].capitalize()
    text2 = name3[3:].capitalize()
    return text1 + text2


# check
print(old_macdonald_sol1('macdonald'))
print(old_macdonald_sol2('macdonald'))
print(old_macdonald_sol3('macdonald'))


# MASTER YODA
def master_yoda(stat):
    my_text = stat.split()
    my_text.reverse()
    # reverse_my_text = my_text[: :-1]
    print(my_text)
    return ' '.join(my_text)


# Check
print(master_yoda('I am home'))
print(master_yoda('we are ready'))


# ALMOST THERE
def almost_there(n):
    return abs(200-n) <= 10 or abs(100-n) <= 10


# Check
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


# LEVEL 2 PROBLEMS
# FIND 33
def has_33(num_list):
    for i in range(len(num_list) - 1):
        if num_list[i] == 3 and num_list[i + 1] == 3:  # num_list[i:i+1] == [3,3]
            return True
    else:
        return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# PAPER DOLL
def paper_doll(str1):
    new_st = ''
    for letter in str1:
        new_st += 3 * letter
    return new_st


print(paper_doll('hello'))
print(paper_doll('Mississippi'))


# BLACKJACK
def blackjack_sol1(a, b, c):
    if 0 < a <= 11 and 0 < b <= 11 and 0 < c <= 11:
        if sum([a, b, c]) <= 21:
            return sum([a,b,c])
        else:
            if 11 in [a, b, c]:
                return sum([a, b, c]) - 10
            else:
                return "BUST"


def blackjack_sol2(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return "BUST"


# print(blackjack_sol1(5, 6, 7))
print(blackjack_sol2(9, 9, 9))
print(blackjack_sol2(9, 11, 8))
# print(blackjack_sol1(9, 11, 8))
# print(blackjack_sol1(11, 11, 10))
print(blackjack_sol2(11, 11, 10))

# SUMMER OF 69
def summer_69(my_list1):
    start_index = 0
    end_index = 0
    for i in range(len(my_list1)):
        if my_list1[i] == 6:
            start_index = i
            print(start_index)
        if my_list1[i] == 9:
            end_index = i + 1
            print(end_index)

    if start_index < end_index:
        del my_list1[start_index:end_index]
        print(my_list1)
        return sum(my_list1)


# SPY GAME
def spy_game_my_sol(num_list):
    for i in range(len(num_list)-2):
        print('i:', i)
        if num_list[i] == 0:
            for j in range(i+1, len(num_list)):
                print('j:', j)
                if num_list[j] == 0:
                    for k in range(j+1, len(num_list)):
                        print('k:', k)
                        if num_list[k] == 7:
                            return True
    else:
        return False


def spy_game(nums):
    zero_counter = 0
    for number in nums:
        if number == 0:
            zero_counter += 1
        elif number == 7 and zero_counter >= 2:
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print('SPY GAME:', spy_game_my_sol([0, 7, 0, 7]))


# COUNT PRIME
def count_prime(n3):
    # 2 is already a prime we start the counter at 1
    prime_num_counter = 1
    for num in range(3, n3+1, 2):
        counter = 0
        for i in range(1, n3, 2):
            if num % i == 0:
                counter += 1
        if counter <= 2:
            prime_num_counter += 1
    return prime_num_counter


print(count_prime(100))






#print(summer_69([4, 5, 6, 7, 8, 9]))
#print(summer_69([1, 3, 5, 2]))
#print(summer_69([2, 1, 6, 9, 11]))
#print(summer_69([2, 3, 6, 6, 9, 10]))

