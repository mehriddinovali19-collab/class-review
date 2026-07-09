class Car:
    def __init__(self, brand: str, model: str|int, year: int):
        self.brand = brand 
        self.model = model
        self.year = year

    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
car = Car("Tayota", "Corolla", 2020)
print(car)