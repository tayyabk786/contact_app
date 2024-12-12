import tkinter as tk #importing tkinter for the GUI
from tkinter import messagebox, simpledialog

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
