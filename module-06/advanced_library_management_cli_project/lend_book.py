import json
from datetime import datetime, timedelta
import save_all_books


def lend_book(all_books):
    book_title = input("Enter Book Title to Lend: ")
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone Number: ")

    for book in all_books:
        if book['title'] == book_title:
            if book['quantity'] > 0:
                due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

                lend_info = {
                    "book_title": book_title,
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "due_date": due_date
                }

                try:
                    with open("lend_books.json", "a") as lend_file:
                        json.dump(lend_info, lend_file)
                        lend_file.write("\n")
                except IOError as e:
                    print(f"Error saving lend data: {e}")

                book['quantity'] -= 1
                save_all_books.save_all_books_funtion(all_books)

                print(f"Book '{book_title}' lent to {borrower_name}. Due date: {due_date}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books

    print("Book not found!")
    return all_books


def return_book(all_books):
    book_title = input("Enter Book Title to Return: ")
    borrower_name = input("Enter Borrower's Name: ")

    try:
        with open("lend_books.json", "r") as lend_file:
            lend_books = lend_file.readlines()

        for lend_info in lend_books:
            lend_data = json.loads(lend_info)
            if lend_data["book_title"] == book_title and lend_data["borrower_name"] == borrower_name:

                lend_books.remove(lend_info)

                for book in all_books:
                    if book['title'] == book_title:
                        book['quantity'] += 1
                        save_all_books.save_all_books_funtion(all_books)

                        with open("lend_books.json", "w") as lend_file:
                            for entry in lend_books:
                                lend_file.write(entry)

                        print(f"Book '{book_title}' returned successfully.")
                        return all_books

        print("No matching lend record found!")
        return all_books
    except IOError as e:
        print(f"Error reading lend books file: {e}")
        return all_books