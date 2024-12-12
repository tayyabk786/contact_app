import tkinter as tk #importing tkinter for the GUI
from tkinter import messagebox, simpledialog

# Contacts variable, making the dictionary
contacts = {}

def add_contact(): #add new contact
    name = simpledialog.askstring("Add Contact", "Enter Name:", parent=root) #for the popup to enter name inside root window
    if not name:
        messagebox.showerror("Error", "Name is required!", parent=root) #if no name entered, popup with error message
        return #stops function from running anymore if no name

    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:", parent=root) #asking user to input phone number
    post_code = simpledialog.askstring("Add Contact", "Enter Postcode:", parent=root) #user inputs postcode
    email = simpledialog.askstring("Add Contact", "Enter Email (optional):", parent=root) #asking user to input email, not mandatory

    contact_info = { #the information getting organized and stored in the dictionary
        "phone": phone, # "phone" stores the phone number
        "post_code": post_code, #"post_code stores postcode"
        "email": email, #stores email
    }

    if name not in contacts:
        contacts[name] = [] #if name is not in contacts dictionary, it creates a new empty list for the name

    contacts[name].append(contact_info) # takes the dictionary including details (contact_info) and adds to list for the name
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!", parent=root) #display success message once contact added

def find_contact(): #defining function for finding contact details
    name = simpledialog.askstring("Find Contact", "Enter Name to Find:", parent=root)
    if not name:
        messagebox.showerror("Error", "Name cannot be empty!", parent=root)
        return

    if name in contacts: #if the name exists in contacts dictionary
        results = "" # initialising empty string to store contact info for name
        for contact in contacts[name]: 
            results += f"Phone: {contact['phone']}\n" #f string to insert phone number in, \n is for new line
            results += f"Address: {contact['post_code']}\n"
            results += f"Email: {contact['email'] if contact['email'] else 'N/A'}\n\n" #if no email was entered then will display N/A

        messagebox.showinfo("Contact Found", f"Name: {name}\n\n{results}", parent=root) #will display contact details
    else:
        messagebox.showinfo("Search Result", f"No contact found with the name '{name}'.", parent=root)# if name entered is not in dictionary






root = tk.Tk() #setting up the GUI
root.title("Contacts App")
root.configure(bg="blue") #background colour 

#setting the window size and center on the screen
app_width = 800
app_height = 600
root.geometry(f"{app_width}x{app_height}") #f string helps fill in the blanks with variables

#the GUI features, with font sizes and padding
title_label = tk.Label(root, text="Contacts App", font=("Times New Roman", 50, "bold")) #font and size 
title_label.pack(pady=20) #.pack places button into the window, pady is for padding (space above and below button)

add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Arial", 18), width=25)
add_button.pack(pady=10)

find_button = tk.Button(root, text="Find Contact", command=find_contact, font=("Arial", 18), width=25)
find_button.pack(pady=10)

show_button = tk.Button(root, text="Show All Contacts", command=show_all_contacts, font=("Arial", 18), width=25)
show_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Arial", 18), width=25)
delete_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 18), width=25, fg="red")
quit_button.pack(pady=20)

root.mainloop() #for running the application until user wants to quit


