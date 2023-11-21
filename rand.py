class book:
    
    book_counter = 0
    
    increase_rate = float(input("enter the increase rate: "))
    
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
    book_counter +=1
    
    def price_increment(self):
        self.price = self.price * book.increase_rate
        return self.price

name_input = str(input("enter the name of the book: "))

author_input  = str(input("enter the name of the author: "))

price_input  = int(input("enter the price of the book: "))
        
book1 = book(name_input,author_input,price_input)
book2 = book("python study","mayaka ombogo",15)

print(f"{book1.name} costs {book1.price}")

book1.price_increment()

print(f" after price increment {book1.name} costs {book1.price}")