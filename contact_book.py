"""
Project: Contact Book

TODO:

1. GUI w/ Tkinter (make it prettier/presentable)
2. File handling
3. Sorting by different features
"""

import re
import tkinter as tk
from tkinter import messagebox

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

    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    try:
        contact_book.append(Contact(name, number, email))
        messagebox.showinfo("Success", "You have successfully added the contact.")
    except ValueError as _:
        messagebox.showerror("Error", str(_))

def view_contact():
    '''Views all the contacts in the contact book.'''

    if len(contact_book) != 0:
        contact_list.delete(0, tk.END)
        for idx, contact in enumerate(contact_book):
            contact_list.insert(tk.END, f"Contact {idx + 1}: {contact.name}, {contact.number}, {contact.email}.")
    else:
        messagebox.showinfo("No Contacts", "You have no contacts yet.")

def search_contact():
    '''Searches for a specific contact in the contact book.'''
    name = name_entry.get()

    found = False
    for contact in contact_book:
        if contact.name == name:
            messagebox.showinfo("Contact Found", f"Here is the contact: {contact.name}, {contact.number}, {contact.email}.")
            found = True
            break
    if not found:
        messagebox.showinfo("Contact Not Found", "I'm sorry, the contact you requested doesn't exist.")

def update_contact():
    '''Updates a singular attribute of a contact in the contact book.'''
    name = name_entry.get()

    found = False
    for contact in contact_book:
        if contact.name == name:
            found = True
            change = change_var.get()
            if change == 1:
                new_name = new_entry.get()
                contact.name = new_name
            elif change == 2:
                try:
                    new_number = new_entry.get()
                    contact.number = new_number
                except ValueError as _:
                    messagebox.showinfo("Invalid Number", str(_))
            elif change == 3:
                try:
                    new_email = new_entry.get()
                    contact.email = new_email
                except ValueError as _:
                    messagebox.showinfo("Invalid Email", str(_))
            else:
                messagebox.showinfo("Invalid Action", "I'm sorry, that action does not exist.")
            break
    if not found:
        messagebox.showinfo("Contact Not Found", "I'm sorry, the contact you have requested doesn't exist.")

def delete_contact():
    '''Deletes a contact in the contact book.'''
    name = name_entry.get()

    found = False
    contact_book_copy = contact_book.copy()
    for contact in contact_book_copy:
        if contact.name == name:
            contact_book.remove(contact)
            messagebox.showinfo("Contact Deleted", "The contact was successfully deleted.")
            found = True
            break
    if not found:
        messagebox.showinfo("Contact Not Found", "I'm sorry, the contact you have requested doesn't exist.")

# Initialize tkinter
root = tk.Tk()
root.title("Contact Book")
root.resizable(True, True)

# Tkinter GUI

name_label = tk.Label(root, text="Contact's Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

number_label = tk.Label(root, text="Contact's Number:")
number_label.grid(row=1, column=0, sticky=tk.W)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="Contact's Email:")
email_label.grid(row=2, column=0, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

new_label = tk.Label(root, text="New Value:")
new_label.grid(row=3, column=0, sticky=tk.W)
new_entry = tk.Entry(root)
new_entry.grid(row=3, column=1)

change_var = tk.IntVar()
change_var.set(1)

change_name_radio = tk.Radiobutton(root, text="Name", variable=change_var, value=1)
change_name_radio.grid(row=4, column=0, sticky=tk.W)

change_number_radio = tk.Radiobutton(root, text="Number", variable=change_var, value=2)
change_number_radio.grid(row=5, column=0, sticky=tk.W)

change_email_radio = tk.Radiobutton(root, text="Email", variable=change_var, value=3)
change_email_radio.grid(row=6, column=0, sticky=tk.W)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=7, column=0, pady=10)

view_button = tk.Button(root, text="View Contacts", command=view_contact)
view_button.grid(row=7, column=1, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=8, column=0)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=8, column=1)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=9, column=0, pady=10)

contact_list = tk.Listbox(root, height=6, width=50)
contact_list.grid(row=10, column=0, columnspan=2, padx=10)

root.mainloop()
