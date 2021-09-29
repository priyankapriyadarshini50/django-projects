poem = """
programming is fun
when the work is done
if you wanna make your work fun:
use Python! """

f = open("myPoem.txt", "w")
f.write(poem)
f.close()

f = open("myPoem.txt", "r")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        print(line, end=' ')


