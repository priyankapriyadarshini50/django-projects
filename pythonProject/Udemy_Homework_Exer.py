def vol(rad):
    return (4/3) * 3.14 * rad ** 3


print(vol(2))


def ran_check(num, low, high):
    if num in range(low, high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'not in the range {low} {high}')
    # return num in range(low, high+1) for boolean value


# Check
ran_check(5, 2, 7)


def up_low(s1):
    # remove all the special character using isalphabet function
    # my_s1_list = [x for x in s1 if x.isalpha()]
    low_counter = 0
    high_counter = 0
    for letter in s1:
        if letter.islower():
            low_counter += 1
        elif letter.isupper():
            high_counter += 1
        else:
            pass

    print('No of upper case characters:', high_counter)
    print('No of lowercase characters:', low_counter)


def up_low_dict_sol(s1):
    d = {'low_counter': 0, 'high_counter': 0}
    for letter in s1:
        if letter.islower():
            d['low_counter'] += 1
        elif letter.isupper():
            d['high_counter'] += 1
        else:
            pass
    print('No of upper case characters:', d['high_counter'])
    print('No of lowercase characters:', d['low_counter'] )


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Check
up_low(s)
up_low_dict_sol(s)


def unique_list(lst):
    return list((set(lst)))


def unique_list_sol2(lst):
    x = []
    for num in lst:
        if num not in x:
            x.append(num)
    return x


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(unique_list_sol2([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    # Remove the spaces from the string
    s1 = s.replace(' ', '')
    reverse_s = s1[::-1]
    return s1 == reverse_s


# Check
print(palindrome('nurses run'))


import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Remove the spaces in the string and convert to lower cases string
    new_str = str1.replace(' ', '').lower()
    # change to set so the repeated letters will get removed
    my_set = set(new_str)
    # make the alphabet list to set for comparison
    alpha_set = set(alphabet)
    return alpha_set == my_set


print(ispangram("The quick brown fox jumps over the lazy dog"))
