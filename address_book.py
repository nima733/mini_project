import csv

contacts = []


def save_contact():
    with open('50-contacts.csv', 'w', newline='') as file:
        header_names = ['first_name', 'last_name', 'company_name', 'address',
                        'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader()
        writer.writerows(contacts)


def view_contacts():
    print('Your Address Book')
    for contact in contacts:
        print(f'Name: {contact["first_name"]}')
        print(f'last_name: {contact["last_name"]}')
        print(f'company_name: {contact["company_name"]}')
        print(f'address: {contact["address"]}')
        print(f'phone: {contact["phone"]}')
        print(f'email: {contact["email"]}')
        print('-' * 30)


def add_contact():
    print('Add new contact:')
    name = input('first_name:')
    last_name = input('last_name:')
    company_name = input('company_name:')
    address = input('address:')
    phone = input('phone:')
    email = input('email:')
    if not phone.isdigit():
        raise ValueError('Phone input must be numeric!')
    contact = {'first_name': name, 'last_name': last_name,
               'company_name': company_name, 'address': address, 'phone': phone,
               'email': email}
    contacts.append(contact)
    save_contact()
    print(f'{name} has been added to contactlist')


def update_contact():
    print('Update a Contact')
    name = input('Enter the name contact for update: ')
    for contact in contacts:
        if contact['first_name'] == name:
            print(f'Current Details for {contact["first_name"]}')
            print(f'Name: {contact["first_name"]}')
            print(f'last_name: {contact["last_name"]}')
            print(f'company_name: {contact["company_name"]}')
            print(f'address: {contact["address"]}')
            print(f'phone: {contact["phone"]}')
            print(f'email: {contact["email"]}')
            print('-' * 30)

            new_name = input('New name: (Press enter to keep current)').strip()
            new_last_name = input(
                'New last name: (Press enter to keep current)').strip()
            company_name = input(
                'New company name: (Press enter to keep current)').strip()
            address = input(
                'New address: (Press enter to keep current)').strip()
            phone = input('New phone: (Press enter to keep current)').strip()
            email = input('New email: (Press enter to keep current)').strip()
            if not phone.isdigit():
                raise ValueError('Phone input must be numeric!')
            if new_name:
                contact['first_name'] = new_name
            elif new_last_name:
                contact['last_name'] = new_last_name
            elif company_name:
                contact['company_name'] = company_name
            elif address:
                contact['address']= address
            elif phone:
                contact['phone'] = phone
            elif email:
                contact['email'] = email
            save_contact()
            print(f'Contact details for {name} has been update ')
            return
    print('------->contact not founded')


def delete_contact():
    print('Delete a contact')
    phone = input('Enter a number contact for delete:')
    if not phone.isdigit():
        raise ValueError('-------->input must be numeric')
    for contact in contacts:
        if contact['phone'] == phone:
            deleted_name = contact['first_name']
            contacts.remove(contact)
            save_contact()
            print(f'{deleted_name} has been deleted from number phone!')

    return

def open_file():
    try:
        with open('50-contacts.csv', 'r') as file:
            lines = csv.DictReader(file)
            for row in lines:
                contacts.append(row)
    except FileNotFoundError:
        print('File does not exist')


open_file()
while True:
    try:
        print('Address Book Menu:')
        print('1. Add contact')
        print('2. View contact')
        print('3. Update contact')
        print('4. Delete contact')
        print('5. Exit')

        user_choice = int(input('Enter Your choice from below option: '))

        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            view_contacts()
        elif user_choice == 3:
            update_contact()
        elif user_choice == 4:
            delete_contact()
        elif user_choice == 5:
            print('Goodbye!')
            exit()
        else:
            print('Invalid choice. Please Try again')

    except Exception as e:
        print(f'Error: {e}')
        print('-' * 30)
