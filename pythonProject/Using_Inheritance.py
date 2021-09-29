class Vehicle:
    """Initializing a vehicle"""
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "White"
        self.capacity = capacity
        self.total_fare = 0
        print(Vehicle.__doc__)
        print("The maximum speed of the vehicle is %d and mileage is %d" % (self.max_speed, self.mileage))
        print("Vehicle Name: %s, Speed : %d, Mileage: %d, Colour : %s" % (self.name, self.max_speed, self.mileage, self.color))

    def seating_capacity(self):
        print("The seating capacity of the vehicle is %d" % self.capacity)

    def fare_charges(self):
        self.total_fare = 100 * self.capacity
        print("Total fare of the vehicle is %d" % self.total_fare)


class Bus(Vehicle):
    """Initializing a Bus"""
    def __init__(self, name, max_speed, mileage):
        self.capacity = 50
        self.final_fare = 0
        print(Bus.__doc__)
        Vehicle.__init__(self, name, max_speed, mileage, capacity=50)

    def bus_fare_charges(self):
        self.final_fare = self.total_fare + self.total_fare * 0.1
        print("The final fare of the Bus is %d" % self.final_fare)


class Car(Vehicle):
    """Initializing a Car"""
    def __init__(self, name, max_speed, mileage):
        self.capacity = 5
        self.final_fare = 0
        print(Car.__doc__)
        Vehicle.__init__(self, name, max_speed, mileage, capacity=5)

    def car_fare_charges(self):
        self.final_fare = self.total_fare + self.total_fare * 0.15
        print("The final fare of the Car is %d" % self.final_fare)


b = Bus('School Volvo', 180, 12)
b.seating_capacity()
b.fare_charges()
b.bus_fare_charges()

c = Car("Audi Q5", 240, 18)
c.seating_capacity()
c.fare_charges()
c.car_fare_charges()
