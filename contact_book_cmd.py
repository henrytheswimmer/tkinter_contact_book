"""
Project: Contact Book

TODO:

1. GUI w/ Tkinter
2. File handling
3. Sorting by different features
"""

import re

contact_book = []


class Contact:
    '''Contact class, creating a layout for every contact in the contact book.'''

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        self.validate_data()

    def validate_data(self):
        '''Validates the email and number of the contact, raising an error if they are invalid.'''
        if not Contact.validate_email(self.email):
            raise ValueError("\nSorry, but you have inputted an invalid email address.\n")

        if not Contact.validate_number(self.number):
            raise ValueError("\nSorry, but you have inputted an invalid phone number.\n")

    @staticmethod
    def validate_email(email) -> bool:
        '''Validates the email of the contact.'''
        valid_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(valid_email, email):
            return False
        return True

    @staticmethod
    def validate_number(number) -> bool:
        '''Validates the number of the contact.'''
        valid_number = r"^\+?[1-9]\d{1,14}$"
        if not re.match(valid_number, number):
            return False
        return True

def add_contact():
    '''Adds a contact to the contact book using user input.'''

    name = input("Contact's Name: ")
    number = input("Contact's Number: ")
    email = input("Contact's Email: ")
    try:
        contact_book.append(Contact(name, number, email))
        print("\nYou have successfully added the contact.\n")
    except ValueError as _:
        print(str(_))

def view_contact():
    '''Views all the contacts in the contact book.'''

    if len(contact_book) != 0:
        for idx, contact in enumerate(contact_book):
            print(f"\nContact {idx + 1}: {contact.name}, {contact.number}, {contact.email}.\n")
    else:
        print("\n You have no contacts yet.\n")

def search_contact():
    '''Searches for a specific contact in the contact book.'''

    name = input("Please provide the name of the contact you are searching for: ")
    found = False
    for contact in contact_book:
        if contact.name == name:
            print(f"\nHere is the contact: {contact.name}, {contact.number}, {contact.email}.\n")
            found = True
            break
    if not found:
        print("\nI'm sorry, the contact you have requested doesn't exist.\n")

def update_contact():
    '''Updates a singular attribute of a contact in the contact book.'''

    name = input("Please provide the name of the contact you want to update: ")
    found = False
    for contact in contact_book:
        if contact.name == name:
            found = True
            change = int(input(f"\nWould you like to change {contact.name}'s 1) name, 2) number, or 3) email?\n"))
            if change == 1:
                new_name = input(f"\nWhat do you want {contact.name}'s new name to be?\n")
                contact.name = new_name
            elif change == 2:
                try:
                    new_number = input(f"\nWhat do you want {contact.name}'s new number to be?\n")
                    contact.number = new_number
                except ValueError as _:
                    print(str(_))
            elif change == 3:
                try:
                    new_email = input(f"\nWhat do you want {contact.name}'s new email to be?\n")
                    contact.email = new_email
                except ValueError as _:
                    print(str(_))
            else:
                print("\nI'm sorry that action does not exist.\n")
            break
    if not found:
        print("\nI'm sorry, the contact you have requested doesn't exist.\n")

def delete_contact():
    '''Deletes a contact in the contact book.'''

    name = input("Please provide the name of the contact you want to delete: ")
    found = False
    contact_book_copy = contact_book.copy()
    for contact in contact_book_copy:
        if contact.name == name:
            contact_book.remove(contact)
            found = True
            break
    if not found:
        print("\nI'm sorry, the contact you have requested doesn't exist.\n")

def run():
    '''Main run function, responsible for all of the methods that the user chooses.'''

    option = int(input("Choose the method you would like to perform: 1) add contact, 2) view contact, 3) search contact, 4) update contact, or 5) delete contact. "))
    if option == 1:
        add_contact()
    elif option == 2:
        view_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        update_contact()
    elif option == 5:
        delete_contact()

print("""
    Welcome to the contact book where you can add, view, search, update, and delete contacts.
    """)
while True:
    run()
