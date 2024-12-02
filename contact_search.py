import contact_view

def search_contact(contact_list):
    s_name = input("Please enter a name  or email or phone number to search contact detail: ")
    li = []
    for contact in contact_list:
        if contact["name"] == s_name or contact["email"] == s_name or contact["phone"] == s_name:
            li.append(contact)

    if li == []:
        print("No result found.")
    else:
        print("Search result: ")
        contact_view.view_contact(li)
        