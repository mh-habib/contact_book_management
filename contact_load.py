import csv

def load_contact(contact_list):
    try: 
        with open("contact_info.csv", "r") as obj_file:
            csv_reader = csv.DictReader(obj_file)
            for row in csv_reader:
                contact_list.append(row)
            return contact_list
    except FileNotFoundError:
        print("Record file not exist!")
        print("Please add contact first.")
    

