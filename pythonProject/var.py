i = 5
print(i)
i = i + 1
print(i)

s = "This is the first line.\nThis is the second line." # one logical line one physical line
p = "This is the first statement.\
This is the second statement." # two physical line, but one logical line
q = "This is the first row"; r = "This is the second row" # two logical statements and one physical statement
print(s)
print(p)
print(q); print(r)
print("Andy\nLucky")
print("Andy", "Lucky")
for i in (0, 2):
    print(i)
else:
    print('*')
x = 1
y = 0
print(x | y)
d1 = {'A': 1, 'B': 2}
d1.clear()
print(d1)
#el = d1.get('A')
#el2 = d1['A']
#print(el)
#print(el2)

#d2 = d1
#del d1
#print(len(d2))

my_list = [1, 2, 3, 4, 5]
del my_list[:]
print(my_list)


def fun(m, n):
    return n
    return n % m


print(fun(2, 5))


def fun1(x):
    var = 3
    print(var + x)


var = 1
fun1(2)
