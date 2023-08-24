import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(length_entry.get())

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    try:
        generated_password = "".join(random.sample(s, plen))
        result_label.config(text="Generated Password: " + generated_password)
    except ValueError:
        messagebox.showerror("Error", "Invalid password length. Please enter a valid length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
