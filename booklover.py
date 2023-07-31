import pandas as pd

class booklover:
    name = ""
    email = ""
    fav_genre = ""
    num_books = 0
    book_list = pd.DataFrame(columns=['book_name', 'book_rating'])
    
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.num_books = num_books
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        
        if (not(self.has_read(book_name))):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print("Book already exists in book_list")
        
    def has_read(self, book_name):
        if ((self.book_list['book_name'].eq(book_name)).any()):
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]