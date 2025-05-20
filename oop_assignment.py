print("---Smartphone Class Challenge output---")
# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life}h battery life."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

# Derived class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate  # in Hz

    def get_info(self):
        # Polymorphism: override method
        base_info = super().get_info()
        return f"{base_info} It has a {self.cooling_system} and {self.refresh_rate}Hz refresh rate."

    def launch_game_mode(self):
        return f"{self.model} has entered Game Mode with max performance!"

# Base class for Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived classes with different move() behaviors
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Function using polymorphism
def move_vehicle(vehicle):
    print(vehicle.move())

# Example usage for both sections
phone1 = Smartphone("Apple", "iPhone 15", 128, 20)
phone2 = GamingSmartphone("ASUS", "ROG Phone 7", 256, 24, "Advanced Cooling", 165)

print(phone1.get_info())
print(phone1.charge())
print(phone2.get_info())
print(phone2.launch_game_mode())

car = Car()
plane = Plane()
boat = Boat()

print("---Polymorphism Challenge output---")

move_vehicle(car)
move_vehicle(plane)
move_vehicle(boat)
