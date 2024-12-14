# def save_all_books_funtion(all_books):
#     with open("all_books.csv",mode="w")as fp:
#         for book  in all_books:
#             line = f"Title: {book['title']}, Author: {book['author']},ISBN: {book['isbn']},Year: {book['year']},Price: {book['price']},Quantity: {book['quantity']}\n"
#             fp.write(line)


import json

def save_all_books_funtion(all_books):
    with open("all_books.json",mode="w") as fp:
        json.dump(all_books,fp,indent=4)

