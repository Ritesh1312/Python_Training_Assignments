
class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self) :
        return f'Book {self.id}--{self.title}'
    
class Books:
    def __init__(self):
        self._books = []

    def add_book(self, id, title, author, price, rating):
        books = Book(id , title, author, price, rating)
        self._books.append(books)


    def find_book_by_id(self, id):
        for book in self._books:
            if book.id == id:
                print(book)
        return None

    def find_books_by_author(self, author):
        matching_books = []
        for book in self._books:
            if book.author == author:
                matching_books.append(book)
        return matching_books
    
    def find_books_in_rating_range(self, min_rating, max_rating):
        matching_books = []
        for book in self._books:
            if min_rating <= book.rating <= max_rating:
                matching_books.append(book)
        return matching_books

    def find_books_in_price_range(self, min_price, max_price):
        matching_books = []
        for book in self._books:
            if min_price <= book.price <= max_price:
                matching_books.append(book)
        return matching_books


if(__name__=='__main__'):
    b = Books()
    b.add_book(1,"Guliver's Travel", "William Shakespeare", 799, 8.1)
    b.add_book(2,"The man who knew Infinity", "Noland", 899, 7.8)
    b.add_book(3,"The Art of Livin", " Bradman ", 599, 7.1)
    b.add_book(4,"Mahabharat", "Ved Vyas", 850, 9.7)
    b.add_book(5,"The story of my Life", "Ritesh", 450,7.7)



    print(b.find_books_in_rating_range(6.0,7.5))
    print(b.find_books_in_price_range(600,900))
    print(b.find_books_by_author("Ritesh"))
 
