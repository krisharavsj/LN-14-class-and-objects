class Vehicle:
    def _init_(self, capacity):
        self.capacity = capacity
        self.base_fare = 50  
    def calculate_fare(self):
        return self.base_fare
class Bus(Vehicle):
    def _init_(self, capacity):
        super()._init_(capacity)
        self.fare_per_person = 10  
    def calculate_fare(self):   
        total_fare = self.base_fare + (self.capacity * self.fare_per_person)
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge
bus1 = Bus(50)
print(f"Total fare for the bus with capacity {bus1.capacity}: ${bus1.calculate_fare()}")
bus2 = Bus(30)
print(f"Total fare for the bus with capacity {bus2.capacity}: ${bus2.calculate_fare()}")