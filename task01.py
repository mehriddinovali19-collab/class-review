class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age 

    
    def introduce(self):
        return f"Hello my name is {self.name} and my age is {self.age}"
    
person = Person("Ali",25)
print(person.introduce())
