import os
import lesson2

def Signin(enteredusername, enteredpassword):
    username = enteredusername # input("Enter a username: ")
    passw = enteredpassword # input("Enter a password: ")

    # formatted string
    # hussainali
    filename = f"{username}.txt"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            savedpass = file.read()
            print(lesson2.hash_password(passw))
            if lesson2.hash_password(passw) == savedpass:
                return "successful login!"
            else:
                return "unsuccessful login, enter password again"


# Create a To-do List program
# todo's writing from the user
# todo's will save the todo's 
# todo's inside file, will be displayed.

def Todo(username):
    filename = f"{username}list.txt"
    todos = []

    # Check if file exists — if yes, read existing todos
    if os.path.exists(filename):
        with open(filename, "r") as file:
            # "take the chicken out of the freezer."
            todos = [line.strip() for line in file.readlines()]
        print(f"📋 Welcome back, {username}! Here are your current to-dos:")
        for i, t in enumerate(todos, start=1):
            print(f"{i}. {t}")
    else:
        print(f"📝 No existing to-do list found for {username}. Creating a new one...")

    # Main input loop
    while True:
        todo = input("\nEnter a new to-do (or type 'exit' to stop): ").strip()
        if todo.lower() == "exit":
            break
        todos.append(todo)

        # 1. take chicken out of freezer
        # 2. go to tuition 
        # 3. study for maths test 
        # 4. bring groceries

        # Display current todos
        print("\nYour current to-dos:")
        for i, t in enumerate(todos, start=1):
            print(f"{i}. {t}")

        # Save to file after each addition
        with open(filename, "w") as file:
            for t in todos:
                file.write(t + "\n")
                # take chicken out of freezer.
                # go to tuition.
                # study for maths test

        choice = input("\nDo you want to add another? (y/n): ").strip().lower()
        if choice != 'y':
            break

    # Final list display
    print("\nFinal To-Do List Saved:")
    for i, t in enumerate(todos, start=1):
        print(f"{i}. {t}")

    print(f"\nAll tasks saved to {filename} ")