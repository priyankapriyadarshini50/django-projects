from random import random, seed, randrange, randint, choice, sample
# print(random())  # produces 0.0 to 1.0 random number
seed()
#  seed(2)
for i in range(5):
    print(random())
print(randrange(6))  # if we provide seed value, the randrange will return the same number at each execution
for j in range(10):
    print(randrange(2, 8), end=' ')
print("\n")
for k in range(10):
    print(randrange(1, 12, 2), end=' ')
print("\n")
print(randint(3, 7))  # it includes both 3 and 7 to produce a random number
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(12):
    print(choice(my_list), end=",")
print("\n")
print(sample(my_list, 7))
