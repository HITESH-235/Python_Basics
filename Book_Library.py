#Create a library that is capable of adding, showing, and taking books using Classes and Objects.

class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.name} was added")

    def show(self):
        if self.books == []:
            print("no books in lib")
        else:
            n = 1
            for x in self.books:
                if x.available == True :
                    print(f"book no.{n} is: {x.name}, author: {x.author}, status: Available")
                    n+=1
                else:
                    print(f"book no.{n} is: {x.name}, author: {x.author}, status: Not Available")
                    n+=1

    def take_book(self,name):
        if self.books == []:
            return "no books in lib"
        else:
            for x in self.books:
                if name == x.name:
                    x.available = False
                    return f"book named {x.name} marked as unavailable"
                else:
                    pass
            return "book not in library"

    def return_book(self,name):
        for x in self.books:
            if name == x.name:
                x.available = True
                return f"book named {x.name} marked as available"


lib = Library()
book1 = Book("book_1","x")
book2 = Book("book_2","y")
book3 = Book("book_3","z")
book4 = Book("book_4","a")
book5 = Book("book_5","b")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib.add_book(book5)

lib.take_book("book_3")
print('\n')
lib.show()
lib.return_book("book_3")
