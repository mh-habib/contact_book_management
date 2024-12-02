def check_duplicate(contact_list, data):
    for contact in contact_list:
        if contact['phone']==data['phone']:
            return True
            