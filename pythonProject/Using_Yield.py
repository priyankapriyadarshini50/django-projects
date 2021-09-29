def generator_test():
    yield "Hello World"


msg = generator_test()
print(msg)
for i in msg:
    print(i)
print(next(generator_test()))
print(list(generator_test()))


def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x


num = even_numbers(10)
print(num)
for j in num:
    print(j)
#print("using next method")
#print(next(num))
#print(next(num))
#print(next(num))
#print(next(num))
#print(next(num))
print(list(num))


