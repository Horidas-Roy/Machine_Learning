class Vehicle:
    vehicles = []
    def __init__(self,vehicle_type,name,speed):
        self.__vehicle_type = vehicle_type
        self.__name = name
        self.__speed = speed
        Vehicle.vehicles.append(self)


    def classify(self):
        return "High-speed Vehicle" if self.__speed > 100 else "Normal Vehicle"
         
    @property
    def get_name(self):
        return self.__name
    @property
    def get_vehicle_type(self):
        return self.__vehicle_type
    @property
    def get_speed(self):
        return self.__speed
    
    
class Car(Vehicle):
    def __init__(self, vehicle_type, name, speed):
        super().__init__(vehicle_type, name, speed)
        print(f"Car Added: {self.get_name}")
    
    def show_info(self):
        print("\n---Vehicle Details---")
        for vehicle in self.vehicles:
            print(f"Type: {vehicle.get_vehicle_type}, Name: {vehicle.get_name}, Speed: {vehicle.get_speed}, Predicted : {vehicle.classify()}")
            

class Bike(Vehicle):
    def __init__(self, vehicle_type, name, speed):
        super().__init__(vehicle_type, name, speed)
        print(f"Bike Added: {self.get_name}")
    
    def show_info(self):
        print("---Vehicle Details---")
        for vehicle in self.vehicles:
            print(f"Type: {vehicle.get_vehicle_type}, Name: {vehicle.get_name}, Speed: {vehicle.get_speed}, Predicted : {vehicle.classify()}")
            

n = int(input())
for i in range(0,n):
    vehicle_type,name,speed = map(str,input().split())
    speed = int(speed)
    if vehicle_type == "Car":
        car = Car(vehicle_type,name,speed)
    else:
        bike = Bike(vehicle_type,name,speed)

car.show_info()