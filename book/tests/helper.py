import random
from book.models import Book

def create_random_book() -> Book:
    return Book.objects.create(
        title = str(random.randint(1111,9999)),
        author = str(random.randint(1111,9999)),
        #year = random.randint(1980,2021),
        category = category,
        status = status
    )
    
def generate_random_books(num_of_books: int) -> list:
    book_list: list = []
    for i in range(num_of_books):
        book: Book = create_random_book()
        book_list.append(book)
        