## Trying out Inheritance 

class Vehcile:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show_details(self):
        print(f"Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}")
        
class Car(Vehcile):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def show_car_details(self):
        self.show_details()
        print(f"Seating Capacity: {self.seating_capacity}")