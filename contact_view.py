def view_contact(contact_list):
    if contact_list == []:
        print("List Is Empty.")
        print("Please Add Contact First!!!")
    else:
        for row in contact_list:
            print(f"Name: {row["name"]} | Email: {row["email"]} | Phone No: {row["phone"]} | Address: {row["address"]}")