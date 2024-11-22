def save_all_books_funtion(all_books):
    with open("all_books.csv","w")as fp:
        for book  in all_books:
            line = f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)