# import csv
# def save_all_contact_function(all_contact):
#     with open("all_contact_book.csv", mode="w", newline="\n", encoding="utf-8") as fp:
#        writer = csv.DictWriter(fp,fieldnames=["name","email","phone_number","address"])
#        writer.writeheader()
#        writer.writerows(all_contact)


import csv

def save_all_contact_function(all_contact):
    try:
        with open("all_contact_book.csv", mode="r", encoding="utf-8") as fp:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    #
    with open("all_contact_book.csv", mode="a", newline="\n", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=["name", "email", "phone_number", "address"])
        if not file_exists:
            writer.writeheader() 
        writer.writerows(all_contact)
