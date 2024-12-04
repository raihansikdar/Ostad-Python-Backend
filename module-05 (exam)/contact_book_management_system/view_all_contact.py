def view_all_contact_function(all_contact: list):
    if all_contact != []:
        print("--------------------**---------------------")
        for contact in all_contact:
           
            print(f"\nName: {contact['name']}, Email: {contact['email']}, Phone No: {contact['phone_number']}, Address: {contact['address']}\n")
        print("--------------------**---------------------")
    else:
        print("\n---------- No contact found in list. ------------\n")
 
           



