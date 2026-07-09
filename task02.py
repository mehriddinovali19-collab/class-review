class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price



    
    def discount(self, percent):
        self.price -= self.price * (percent / 100)
        return self.price
    

book = Book("Python Crash Course", "Eric Matthes", 50)
new_price = book.discount(20)
print(new_price)
        