import add_to_file
import contact_duplicate

def add_contact(contact_list):
    name = input("Enter Name: ")
    if name.isdigit() == True:
        print("Please enter a valid name.")
        print("It will not be only number!")
        name = input("Enter Name: ")
    if name.isdigit() == True:
        print("Please enter a valid name.")
        print("It will not be only number!")
        name = input("Enter Name: ")
    if name.isdigit() == True:
        print("Please enter a valid name.")
        print("It will not be only number!")
        name = input("Enter Name: ")
    if name.isdigit() == True:
        print("Maximum wrong attempt!")
        print("Please try again letter!!!")
        return

    email = input("Enter Email: ")
    if ("@" in email and "." in email and email.islower()) == False:
        print("Please enter a valid email address!")
        email = input("Enter Email: ")
    if ("@" in email and "." in email and email.islower()) == False:
        print("Please enter a valid email address!")
        email = input("Enter Email: ")
    if ("@" in email and "." in email and email.islower()) == False:
        print("Please enter a valid email address!")
        email = input("Enter Email: ")
    if ("@" in email and "." in email and email.islower()) == False:
        print("Maximum wrong attempt!")
        print("Please try again letter!!!")
        return

    phone = input("Enter Phone Number: ")
    if phone.isdigit() == False:
        print("Please enter phone number only!")
        phone = input("Enter Phone Number: ")
    if phone.isdigit() == False:
        print("Please enter phone number only!")
        phone = input("Enter Phone Number: ")
    if phone.isdigit() == False:
        print("Please enter phone number only!")
        phone = input("Enter Phone Number: ")
    if phone.isdigit() == False:
        print("Maximum wrong attempt!")
        print("Please try again letter!!!")
        return
    
    address = input("Enter Address: ")

    data={
        "name" : name,
        "email" : email,
        "phone" : phone,
        "address" : address
    }

    if contact_duplicate.check_duplicate(contact_list, data) == True:
        print(f"{data["phone"]} => Contact already exist!!")
    else:
        contact_list.append(data)
        add_to_file.save_to_file(contact_list)
        print("Contact information added successfully!")
    