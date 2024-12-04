import csv

def search_contact_function(phone_to_search: int):
    try:
        with open("all_contact_book.csv", mode="r", encoding='utf-8') as fp:
            fpReader = csv.DictReader(fp)  
            found = False     
            
            for contact in fpReader:
                if contact['phone_number'] == str(phone_to_search):  
                    print("----------- Contact Details: ------------")
                    print(contact)
                    found = True
                    break  
       
            if not found:
                print("--------- Contact not found! ---------")
    
    except FileNotFoundError:
        print("Error: The file 'all_contact_book.csv' was not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")