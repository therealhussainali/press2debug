import os
import lesson2

def Register(enteredusername, enteredpassword):
    username = enteredusername
    password = enteredpassword

    # formatted string
    thefilename = f"{username}.txt"

    # validation check to see if the user/file already exists
    if os.path.exists(thefilename) == True:
        return "Username already exists!"
    else:
        with open(thefilename, 'w') as file:
            file.write(lesson2.hash_password(password))
    return f"User '{username}' created successfully"
    # print(f"Password saved in '{thefilename}'")