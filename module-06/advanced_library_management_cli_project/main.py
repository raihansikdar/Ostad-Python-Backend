import add_books
import view_all_books
import restore_all_files
import update_book_file
import delete_book_file
import lend_book

all_books = []

while True:
    print("\n---- Welcome to Advanced  Library Management System----\n")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete/Remove Book")
    print("5. Lend Book")
    print("6. Return Book")

    all_books = restore_all_files.restore_all_books(all_books)

    menu = input("Select an option: ")
    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books_funtion(all_books)

    elif menu == "2":
        view_all_books.view_all_books_function(all_books)

    elif menu == "3":
        all_books = update_book_file.update_books_function(all_books)

    elif menu == "4":
        all_books = delete_book_file.delete_books(all_books)

    elif menu == "5":
        all_books = lend_book.lend_book(all_books)

    elif menu == "6":
        all_books = lend_book.return_book(all_books)
    else:
        print("Choose a valid number")