class Car: 
    def __init__(self,brand , model):
        self.brand = brand
        self.model = model 
    def full_name(self): 
        return f"{self.brand} {self.model}"
    

my_car = Car("Toyota", "corolla")
print(my_car.brand)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())


# self provide the context of the object for which it has called the class variable it is also known as "this" in js like language
# __init__ is act as constructor in python 