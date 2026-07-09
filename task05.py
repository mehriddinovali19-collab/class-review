class Animal:
    def __init__(self, name: str):
        self.name = name


    
    def sound(self):
        print(f"{self.name}Sound are going out!")


class Dog(Animal):

    def sound(self):
        print(f"{self.name}:  WOW WOW")
        return
    

class Cat(Animal):

    def sound(self):
        print(f"{self.name}:  Meo meo meo")


dog = Dog("Dog")
dog.sound()

cat = Cat("Cat")
cat.sound()