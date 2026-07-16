# class

class Car :
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
    def aboutName (self):
        return f"{self.brand} and it's modle is {self.model}"

car = Car("BMW" , "M5")

print(car.aboutName())

class Electronic_Car(Car):
    def __init__(self, brand, model, battery_size ):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def aboutElectronic(self):
        return f"{self.brand} and it's modle is {self.model}, and it's Battery Size is {self.battery_size}";

elect_car = Electronic_Car("BMW" , "M5" , "19k KHW")

print(elect_car.aboutElectronic())