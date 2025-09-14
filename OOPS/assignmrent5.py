#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

b1 = book("1984","George Orwell",1949)
b2 = book("To Kill a Mockingbird","Harper Lee",1960)

(b1.display_info())
b2.display_info()