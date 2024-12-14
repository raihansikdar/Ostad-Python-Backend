from save_all_books import save_all_books_funtion
import random
from datetime import datetime

def add_books_funtion(all_books):
    title = input("Enter book title : ")
    author = input("Enter book author name : ")
    isbn = random.randint(1000,99999)
    year = int(input("Enter book publishing year : "))
    price = int(input("Enter book price : "))
    quantity = int(input("Enter Quantity number : "))
    bookAddedTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title, 
        "author": author,
        "isbn": isbn, 
        "year": year,
        "price":price,
        "quantity": quantity,
        "bookAddedTime": bookAddedTime
    }

    all_books.append(book)
    save_all_books_funtion(all_books)

    print("Books added successful")
    return all_books