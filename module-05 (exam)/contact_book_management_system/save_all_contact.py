# import csv

# header = ['Name', 'Email', 'Phone', 'address']

# def save_all_contact_function(all_contact):
#     with open("all_contact_book.csv", mode="w", newline="\n", encoding="utf-8") as fp:
#         write_file = csv.writer(fp)
#         write_file.writerow(header)
        
#         for contact in all_contact:
#             line = [contact['name'], contact['email'], contact['phone_number'], contact['address']]
#             write_file.writerow(line)

import csv
def save_all_contact_function(all_contact):
    with open("all_contact_book.csv", mode="w", newline="\n", encoding="utf-8") as fp:
       writer = csv.DictWriter(fp,fieldnames=["name","email","phone_number","address"])
       writer.writeheader()
       writer.writerows(all_contact)
