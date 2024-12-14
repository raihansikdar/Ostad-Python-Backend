import datetime
import save_all_books


def update_books_function(all_book):
    search_book = input("Enter Book Title to Update: ")

    for book in all_book:
        if search_book == book["title"]:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))
            book_last_updated_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["book_last_updated_time"] = book_last_updated_time

            save_all_books.save_all_books_funtion(all_books=all_book)

            print("--- Book Update Successfully ---")
            return all_book
    
    print("Book Not Found")

