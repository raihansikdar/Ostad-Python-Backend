import csv

def load_all_contact_function():
    try:
        with open("all_contact_book.csv", mode="r", encoding='utf-8') as fp:
            fpReader = csv.reader(fp)
            contacts = list(fpReader)  

            if contacts == []:  
                print("------------The contact book is empty.------------")
                return
            
            print("--------------------**---------------------")
            for contact in contacts:
                print(contact)
            print("--------------------**---------------------")
            
    except FileNotFoundError:
        print("--The file 'all_contact_book.csv' was not found. Please ensure the file exists.--")
    except Exception as e:
        print(f"---An unexpected error occurred: {e}---")