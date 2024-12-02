import contact_load
import contact_add
import contact_view
import contact_remove
import contact_search

contact_list = []
contact_load.load_contact(contact_list)

while True:
    print("Welcome To My Contact Management Project.")
    print("Use 0 to exit app")
    print("Use 1 to add contact")
    print("Use 2 to view contact")
    print("Use 3 to remove contact")
    print("Use 4 to search contact")

    try:
        option = int(input("Please Enter a Number to Select Operation: "))
        if option == 0:
            print("Thanks for using my contact management app.")
            break
        elif option == 1:
            contact_add.add_contact(contact_list)
        elif option == 2:
            contact_view.view_contact(contact_list)
        elif option == 3:
            contact_remove.remove_contact(contact_list)
        elif option == 4:
            contact_search.search_contact(contact_list)
        else:
            print("Please enter a valid number to specify operation!")    
    except ValueError:
        print("Please Enter a vallid Number.")