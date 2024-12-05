import save_all_contact
import csv

def add_contact_function(add_contact):

   try:

        name = input("Enter name : ").strip()
        if not all(part.isalpha() for part in name.split()):
            raise ValueError('-----Name must be string-----')
        
        email = input("Enter email : ").strip()
        
        phone_number = input("Enter Phone Number : ").strip()
        if not phone_number.isdigit():
            raise ValueError("----Phone number must be numeric.---")
        
        # # Check for duplicate phone numbers
        # if any(contact["phone_number"] == phone_number for contact in add_contact):
        #     raise ValueError("This phone number already exists in the contact book.")
        
        address = input("Enter Address : ").strip()
        
        contact_book = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address
        }

        phone_exist = check_phone_no_exist_function(phone_number_exist= phone_number)

        if phone_exist:
            print("\n----------- This phone number already exists in the contact book. -------------\n")

        else:
            add_contact.append(contact_book)
            save_all_contact.save_all_contact_function(add_contact)
            print("\n----------- Contact added successful -------------\n")
            return add_contact

   except ValueError as e:
      print(f"{e}")
      print(f"-------Input Guidencs---------")
      print("Name: String"),
      print("Email: String"),
      print("Phone Number: Digit(int)"),
      print("Address: String"),
      print(f"--------------X----------------")
      
      return add_contact
      



def check_phone_no_exist_function(phone_number_exist: int):
    try:
        with open("all_contact_book.csv", mode="r", encoding='utf-8') as fp:
            fpReader = csv.DictReader(fp)  
          
            for contact in fpReader:
                if contact['phone_number'] == str(phone_number_exist):  
                   return True
                else:
                    return False
    
    except FileNotFoundError:
        # print("Error: The file 'all_contact_book.csv' was not found. Please ensure the file exists.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


