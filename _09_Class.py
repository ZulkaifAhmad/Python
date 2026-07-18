class Car:
    def __init__(self, brand, model):
        self._brand = brand      # single underscore
        self._model = model
        
    @staticmethod # decorators
    def introduction():
        return "Hello to Introduction"
    
    def aboutName(self):
        return f"{self._brand} and it's model is {self._model}"


class Electronic_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self._battery_size = battery_size

    def aboutElectronic(self):
        return f"{self._brand} and it's model is {self._model}, and it's Battery Size is {self._battery_size}"


car = Car("BMW", "M5")
print(car.aboutName())
print(Car.introduction())

elect_car = Electronic_Car("BMW", "M5", "19k KWh")
print(elect_car.aboutElectronic())  # you also forgot to print this


