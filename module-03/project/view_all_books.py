# def view_all_books_function(all_books):
#     if all_books != []:
#         for book in all_books:
#             print(f"Title : {book['title']}, Author : {book['author']}, ISBN {book['isbn']}, Year : {book['year']}, Price : {book['price']}, Quantity: {book['quantity']}")
#     else:
#         print("No Book found in All Boks file")

import csv
def view_all_books_function(all_books):
    with open("all_books.csv",mode="r")as fp:
        fpReader = csv.reader(fp)

        for book in fpReader:
            print (book)
            


