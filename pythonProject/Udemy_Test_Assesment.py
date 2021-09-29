st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)


def even_fun():
    for num in range(0, 11):
        if num % 2 == 0:
            print(num)


even_fun()
mylist = [x for x in range(1, 51) if x % 3 == 0]
print(mylist)


def even_word():
    st1 = 'Print every word in this sentence that has an even number of letters'
    for word1 in st1.split():
        if len(word1) % 2 ==0:
            print(word1, "is Even!")


even_word()


def fizz_buzz():
    for i in range(1, 100):
        if i % 3== 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3== 0 and i % 5 == 0:
            print("FizzBuzz")


#fizz_buzz()


my_st = 'Create a list of the first letters of every word in this string'
result = [element[0] for element in my_st.split()]
print(result)


# RETURNS TRUE IF ANY NUMBER IN THE LIST IS EVEN
def even_check(test_list):
    for num in test_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False


print(even_check([1, 3, 5]))
print(even_check([2, 3, 4]))


# RETURN A LIST OF EVEN NUMBERS FROM AN INPUT LIST
def even_check_list(my_list):
    even_list = []
    for num in my_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list


print(even_check_list([1, 2, 3, 40, 55, 200]))


# RETURNS A STRING WITH EVEN LETTER IN UPPERCASE AND ODD LETTER IN LOWER CASE
def myfunc(str1):
    result_str = ''
    for i in range(len(str1)):
        if i % 2 == 0:
            up_letter=str1[i].upper()
            result_str +=up_letter

        else:
            low_letter=str1[i].lower()
            result_str +=low_letter
    return result_str

print(myfunc('Priyanka'))
