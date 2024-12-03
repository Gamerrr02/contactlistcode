import datetime
import sys
import re
 
# Function to validate phone number format
def validate_phone_number(phone_number: str) -> bool:
    return bool(re.match(r"^\d{11}$", phone_number))  # Adjust regex as per the format required
 
def validate_email(email: str) -> bool:
    # Regex for basic email validation
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))
 
def add_contact():
    add_new_contact = False
    print("=== Add A New Contact ===")
   
    while not add_new_contact:
        fname = input("Enter their firstname: ")
        sname = input("Enter their surname: ")
        phone_number = str(input("Enter their phone number (11 digits): "))
        email = str(input("What is their email?: "))
 
        if not validate_phone_number(phone_number):
            print("Invalid phone number format. Please enter a 11-digit number.")
            continue
 
        if not validate_email(email):
            print("Invalid email format. Please enter an @ in the email.")
            continue
 
        # Save user data
        with open('savedcontacts', 'a') as file:
            file.write(f"{fname}:{sname}:{phone_number}:{email}\n")
        print("Contact Saved Successfully. Saving data...")
        add_new_contact = True
 
def contact_search():
    print("First_Name   Surname   Phone_Number    Email")
    f = open("savedcontacts", "r")
    print(f.read())
 
def main():
    # Menu options in a loop
    while True:
        print("==========MENU==========")
        print("[1] Add A New Contact")
        print("[2] Search Contacts")
        print("[3] Quit")
       
        option = input("Choose your option: ")
       
        if option == "1":
            add_contact()
        elif option == "2":
            contact_search()
        elif option == "3":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option. Please choose again.")
 
if __name__ == "__main__":
    main()
