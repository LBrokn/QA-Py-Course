class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with  {len(self.books)} books."
    

shelf = BookShelf(300)

class Book(BookShelf):
   def __init__(self, name):
     self.name = name

   def __str__(self):
       return f"Book {self.name}"

book = Book("Example")
book2= Book("Example 2")
shelf= BookShelf(book, book2)

print(shelf)