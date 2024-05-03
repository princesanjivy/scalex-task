from model.book import Book
import csv

def get_regular_books():
    books = []
    with open("./data/regularUser.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            books.append(Book(**row))
    return books

def get_admin_books():
    books = []
    with open("./data/adminUser.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            books.append(Book(**row))
    return books

# above functions can be clubbed together into single with a parameter for the file name,
# but, I prefer keeping it as separate functins to improve readbility

def add_book(book: Book):
    with open("./data/regularUser.csv", mode="a", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([book.book_name, book.author, book.publication_year])
    
def remove_book(book_name: str) -> int: # an int is return to figure about is anything deleted or not
    books = get_regular_books()
    filtered_books = [book for book in books if book.book_name.lower() != book_name.lower()]
    # print(len(filtered_books),len(books))
    if len(filtered_books) == len(books):
        return 0
    else:
        with open("./data/regularUser.csv", mode="w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Book Name", "Author", "Publication Year"])
            for book in filtered_books:
                csv_writer.writerow([book.book_name, book.author, book.publication_year])
        return 1
