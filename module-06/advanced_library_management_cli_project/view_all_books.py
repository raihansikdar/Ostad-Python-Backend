import json

def view_all_books_function(all_books):
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)
        if all_books:
            for book in all_books:
                print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedTime']}")
        else:
            print("\n---No Book found ----")



