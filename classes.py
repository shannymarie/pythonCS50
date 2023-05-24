class Point():
    # init function is automaticly called
    def __init__(self, inputx, inputy):
        self.x = inputx
        self.y = inputy

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        # list of passengers
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)



p = Point(2,8)

print(p.x)
print(p.y)

flight = Flight(3)

people = ["Harry", "Ron","Hermione","Ginny"]
for person in people:
    # adding passengers to the flight
    succes = flight.add_passenger(person)
    if succes:
        print(f"person {person} added succesfully")
    else:
        print(f"no available seats for {person}")