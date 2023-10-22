#simple bookstore with oops concept

class Bookstore:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def addBook(self):
        print('Added book details:')
        print('Title :',self.title)
        print('Author :',self.author)
        print('Isbn number :',self.isbn)
    
    def borrowBook(self):
        print('Borrowed book details:')
    
    def returnBook(self):
        pass
    
list_of_books = []
print('Welcome to bookstore!')
while True:
    option = int(input('How can we help you ?: \n1.Add a book.\n2.Borrow book.\n3.Return a book.\n4.Quit\n\n'))

    if option != 4:
        title = input('Enter book title.')
        author = input('Enter author name.')
        isbn = input('Enter isbn number.')

    if option == 1:
        b = Bookstore(title,author,isbn)
        for book in list_of_books:
            if isbn in book[isbn]:
              print('Book already in library.')
            else:
              b.addBook()
              list_of_books.append(b)
              print('Book added successfully.')

    elif option == 2:
        pass
    
    elif option == 4:
        break