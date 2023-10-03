
class Book:
    def __init__(self, id, title, author, price, rating):
        self._id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

class Books:
    def __init__(self):
        self.books = []

    def find_book_by_id(books, id):
        for book in books:
            if book.id == id:
                return book
        return None

    def find_books_by_author(books, author):
        matching_books = []
        for book in books:
            if book.author == author:
                matching_books.append(book)
        return matching_books
    
    def find_books_in_rating_range(books, min_rating, max_rating):
        matching_books = []
        for book in books:
            if min_rating <= book.rating <= max_rating:
                matching_books.append(book)
        return matching_books

    def find_books_in_price_range(books, min_price, max_price):
        matching_books = []
        for book in books:
            if min_price <= book.price <= max_price:
                matching_books.append(book)
        return matching_books