import csv

def save_to_file(contact_list):
    field_name = ['name', 'email', 'phone', 'address']
    with open("contact_info.csv", "w", newline="") as obj_file:
        csv_writter = csv.DictWriter(obj_file, fieldnames=field_name)
        csv_writter.writeheader()
        csv_writter.writerows(contact_list)