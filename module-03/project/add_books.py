from save_all_books import save_all_books_funtion


def add_books_funtion(all_books):
    title = input("Enter book title : ")
    author = input("Enter book author name : ")
    isbn = int(input("Enter book ISBN number : "))
    year = int(input("Enter book publishing year : "))
    price = int(input("Enter book price : "))
    quantity = int(input("Enter Quantity number : "))

    book = {
        "title": title, 
        "author": author,
        "isbn": isbn, 
        "year": year,
        "price":price,
        "quantity": quantity
    }

    all_books.append(book)
    save_all_books_funtion(all_books)

    print("Books added successful")
    return all_books