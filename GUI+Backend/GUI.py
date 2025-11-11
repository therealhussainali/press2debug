import tkinter as tk
from tkinter import messagebox
from login import Signin
from signup import Register
from login import fetch_todos
from login import add_todo
from login import Signup

def open_todo_window(username):
    todo_window = tk.Toplevel()
    todo_window.title(f"{username}'s To-Do List")
    todo_window.geometry("400x420")
    todo_window.resizable(False, False)

    # Title
    tk.Label(todo_window, text=f"{username}'s To-Do List", font=("Arial", 14, "bold")).pack(pady=10)

    # Listbox to show tasks
    listbox = tk.Listbox(todo_window, width=45, height=15)
    listbox.pack(pady=10)

    # Entry to add new task
    entry = tk.Entry(todo_window, width=35)
    entry.pack(pady=5)

    # Button frame
    btn_frame = tk.Frame(todo_window)
    btn_frame.pack(pady=10)

    # Placeholder local storage (in-memory for now)
    todos = []
    todos = fetch_todos(username)

    for i, t in enumerate(todos, start=1):
        listbox.insert(tk.END, t)
        entry.delete(0, tk.END)

    # Add Task
    def add_task():
        task = entry.get().strip()
        if task: #check if its null or not.
            add_todo(username, task)
            todos.append(task)
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    # Delete Task
    def delete_task():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            todos.pop(index)
            listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    # Buttons
    tk.Button(btn_frame, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task).grid(row=0, column=1, padx=5)

    # Exit Button
    tk.Button(todo_window, text="Logout", width=12, command=todo_window.destroy).pack(pady=10)



# GUI -> BACKEND -> CALLS API -> API ADDS/GETS INFORMATION FROM DATABASE
# 3 processes are running

# --- Login / Signup Window ---
def login_ui():
    root = tk.Tk()
    root.title("To-Do App | Login")
    root.geometry("350x230")
    root.resizable(False, False)

    tk.Label(root, text="Welcome to To-Do App", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(root, text="Username:", font=("Arial", 10)).pack(pady=2)
    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=2)

    tk.Label(root, text="Password:", font=("Arial", 10)).pack(pady=2)
    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=2)

    # Placeholder login/signup functions
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        result = Signin(username, password)

        messagebox.showinfo("Login", result)

        if result == "Successful Login":
            root.withdraw()  # hide login window
            open_todo_window(username)

    def handle_signup():
        username = username_entry.get().strip()
        password = password_entry.get()
        result = Signup(username, password)

        messagebox.showinfo("Sign Up", result)
        if result == "Successful Signup":
            root.withdraw()
            open_todo_window(username)

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Login", width=12, command=handle_login).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Sign Up", width=12, command=handle_signup).grid(row=0, column=1, padx=5)

    root.mainloop()


# Run app
if __name__ == "__main__":
    login_ui()