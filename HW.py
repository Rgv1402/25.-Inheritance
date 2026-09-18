class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand  = brand
        self.max_speed = max_speed
    def show_details(self):
        print("Brand:", self.brand)
        print("Max Speed: ", self.max_speed)
    
class Car(Vehicle):
    def __init__(self, model, seats, brand, max_speed):
        self.model = model
        self.seats = seats
        super().__init__(brand, max_speed)
    def show_details(self):
        print("Model: ", self.model)
        print("Seats: ", self.seats)
        super().show_details()
    def fuel_type(self, fuel):
        self.fuel = fuel
        print(self.model,"uses", fuel)

carr = Car("Camry", 5, "Toyota", 180)
carr.show_details()
carr.fuel_type(input("\nEnter fuel type:"))

print("\nIs car subclass of Vehicle? ", issubclass(Car, Vehicle))