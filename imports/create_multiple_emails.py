from create_email import create_email 

def create_multiple_emails(lists):
    new_list = []
    for my_list in lists:
        new_list.append(create_email(my_list))
    
    return new_list