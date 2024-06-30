# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):
    older = book1 if book1.year < book2.year else book2 if book2.year < book1.year else 'same'
    if older == 'same':
        print(f'{book1.name} and {book2.name} were published in {book1.year}')
    else:
        print(f'{older.name} is older, it was published in {older.year}')