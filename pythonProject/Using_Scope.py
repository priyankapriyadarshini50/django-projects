name = 'THIS IS A GLOBAL STRING' # GLOBAL

def greet():
    # name = 'Sammy' # Enclosing function LOCAL
    def hello():
        # name = 'Sally' # LOCAL within function
        print('Hello '+name)
    hello()


greet()


