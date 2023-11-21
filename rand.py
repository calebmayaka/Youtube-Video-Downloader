
class book:
    books_present = 0
    increment_value = float(input('Enter the increment value'))
    
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
        
    books_present += 1
    
    def price_increment(self):
        self.price = book.increment_value * self.price
        return self.price

input_name = str(input("enter the name of the book"))
input_author = str(input("enter the name of the book"))
input_price = int(input("enter the name of the book"))


book1 = book(input_name, input_author, input_price)

print(f"the name of the boook is {book1.name} and the author is {book1.author} and the price is {book1.price} ")

book1.price_increment()

print(f"the new price is {book1.price}")
    
    
