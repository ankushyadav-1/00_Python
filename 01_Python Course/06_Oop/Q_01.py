class Car:
    total_car = 0


    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Disel"
    
    @staticmethod
    def gernal():
        return "Cars are cool."
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battrey_size):
        super().__init__(brand, model)
        self.battrey_size = battrey_size

    def fuel_type(self):
        return "Electric Charge"



my_tesla = ElectricCar("Tesla", "Modle S", "85kWh")
# print(my_tesla.__brand)
# print("Your Car Need", my_tesla.fuel_type())

my_car = Car("Tata", "Safari")
Car.model = "kalu"
# print("Fuel Type for Your Car is",my_car.fuel_type())

# print(Car.total_car)
# print(Car.gernal())

print(my_car.model)



# my_car1 = Car("Toyota", "Corolla")
# print(my_car1.brand)
# print(my_car1.model)
# print(my_car1.name())