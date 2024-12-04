import add_contacts
import view_all_contact
import remove_contact
import search_contact
import load_all_contact

contact_book_list = []

while True:
    print("Welcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add contact")
    print("2. View All contact")
    print("3. load All contact")
    print("4. Remove contact") 
    print("5. Search contact") 


    menu = input("Select any number: ")

    if menu == '0':
        print("Thanks for using Contact Book Managemnt System")
        break
    
    elif menu == "1":
          contact_book_list = add_contacts.add_contact_function(contact_book_list)
    elif menu == "2":
         view_all_contact.view_all_contact_function(all_contact= contact_book_list)
    elif menu == "3":
         load_all_contact.load_all_contact_function()
    elif menu == "4":
         phone_to_remove = int(input("Enter phone number to remove : "))
         remove_contact.remove_contact_function(phone_to_remove = phone_to_remove,all_contact= contact_book_list)
    elif menu == "5":
         phone_to_search = int(input("Enter phone number to search : "))
         search_contact.search_contact_function(phone_to_search = phone_to_search)
    else:
         print("Choose a valid number")

