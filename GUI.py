import tkinter as tk
from tkinter import messagebox
from login import Signin
from signup import Register

def login():
    username = username_entry.get().strip()
    password = password_entry.get()
    result = Signin(username, password)

    messagebox.showinfo("Login", result)

def register():
    username = username_entry.get().strip()
    password = password_entry.get()
    result = Register(username, password)

    messagebox.showinfo("Sign Up", result)

# Main window
root = tk.Tk()
root.title("Login / Sign Up")
root.geometry("520x600")

# Username label and entry
tk.Label(root, text="Username:", font=("Times New Roman", 30)).pack(pady=15)
username_entry = tk.Entry(root, width=50)

username_entry.pack()

# Password label and entry
tk.Label(root, text="Password:", font=("Arial", 10)).pack(pady=5)
password_entry = tk.Entry(root, width=30, show="&")
password_entry.pack()

# Frame for buttons side by side
btn_frame = tk.Frame(root)
btn_frame.pack(pady=30)

tk.Button(btn_frame, text="Login", width=10, command=login).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Sign Up", width=10, command=register).grid(row=0, column=1, padx=10)

root.mainloop()