class Person:
    """This class represents the population of a city"""
    population = 0

    def __init__(self, name, age):
        """"This method initializing a person's data"""
        self.name = name
        self.age = age
        print(Person.__init__.__doc__)
        print('%s\'s age is %d' %(self.name, self.age))
        Person.population = Person.population + 1

    def sayhi(self):
        """"Greetings from the newly added person"""
        print(Person.sayhi.__doc__)
        print("Hi, my name is %s" % self.name)

    def howmany(self):
        """Prints the current population"""
        print(Person.howmany.__doc__)
        if Person.population == 1:
            print("I am the only one person in the city!")
        else:
            print("The total number of population is %d" % Person.population)

    def __del__(self):
        """The person is leaving the city"""
        print(Person.__del__.__doc__)
        Person.population = Person.population - 1
        if Person.population == 0:
            print("I am %s, the last one in the city!" % self.name)
        else:
            print("Still there are %d much people left" % Person.population)


print(Person.__doc__)
p = Person("Priyanka", 34)
p.sayhi()
p.howmany()

p1 = Person("Umesh", 42)
p1.sayhi()
p1.howmany()
p1.age = 43
print("%s's modified age is %d" %(p1.name, p1.age))

p2 = Person("Adya", 4)
p2.sayhi()
p2.howmany()

