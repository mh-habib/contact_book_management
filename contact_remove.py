import add_to_file

def remove_contact(contact_list):
    r_phone = input("Enter a phone number to remove from contact book: ")
    found = False
    flag = 0
    for row in contact_list:
        if row['phone'] == r_phone:
            found = True
            contact_list.pop(flag)
            add_to_file.save_to_file(contact_list)
            print(f"{row['phone']} => Contact removed successfully!!!")
            return
        flag = flag  + 1
    if found == False:
            print("Contact not found!!!")