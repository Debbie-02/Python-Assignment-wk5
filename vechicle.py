# Base class (using polymorphism & inheritance)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("This vehicle moves in some way.")

# Child classes
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def move(self):
        print(f"The car {self.brand} {self.model} is driving 🚗")

class Plane(Vehicle):
    def __init__(self, brand, model, airline):
        super().__init__(brand, model)
        self.airline = airline

    def move(self):
        print(f"The plane {self.brand} {self.model} is flying ✈️")

class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type

    def move(self):
        print(f"The boat {self.brand} {self.model} is sailing 🚤")

# Main Program
if __name__ == "__main__":
    car1 = Car("corolla", "Tesla", "Honda")
    plane1 = Plane("Boeing", "Airbus", "Helicopter")
    boat1 = Boat("Submarine", "Yacht", "Jet Ski")

    # Polymorphism in action
    for vehicle in (car1, plane1, boat1):
        vehicle.move()