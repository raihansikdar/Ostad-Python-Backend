import add_books
import view_all_books

all_booksList = []

while True:
    print("Welcome to library Management System")
    print("0. Exit")
    print("1. Add books")
    print("2. View All Books")


    menu = input("Select any number: ")

    if menu == '0':
        print("Thanks for using library Managemnt System")
        break
    
    elif menu == "1":
         all_booksList= add_books.add_books_funtion(all_booksList)
    elif menu == "2":
         view_all_books.view_all_books_function(all_booksList)
    else:
         print("Choose a valid number")