# this program is going to use break and continue
running = True
while running:
    s = input("Enter a string value:")
    if s == 'quit':
        print('The loop breaks here')
        continue
    else:
        x = len(s)
        print('The length of the string:', x)
else:
    print('Exit from while loop')
