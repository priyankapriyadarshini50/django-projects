print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))

if __name__ == '__main__':
    print("This program is run by itself.")
else:
    print("I am being imported from another module.")
