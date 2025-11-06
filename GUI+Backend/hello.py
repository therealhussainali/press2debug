# Create a user password system. 
# 1. User input login/sign up 
# 2. create a file for each user according to their username "hussain.txt" FOR sign up and print password to file
# 3. you will go into the user file "umair.txt" and read the password. 

# file handling library
import os
import hashlib

# User I/O 
# Ask user if he wants to login or sign up. 
print("Welcome! Do you want to login or sign up?")
choice = input("Type 'login' or 'signup':").lower()

    if choice == "signup":
        # get input of user of username and password
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        # formatted string
        filename = f"{username}.txt"

        # validation check to see if the user/file already exists
        if os.path.exists(filename) == True:
            print("Username already exists!")
        else:
            with open(filename, 'w') as file:
                file.write(password)
        print(f"User '{username}' created successfully")
        print(f"Password saved in '{filename}'")
    elif choice == "login":
        # project karke aana hai

        # I/O username password
        # declare filename variable
        # check if file exists against username
        # close if username does not exist. 55
        # open file, read the file 
        # compare the read password vs the inputted password
        # same password equals "successfull login"
        # not same "wrong password"

        print("hello login")
    else:
        print("ERROR Invalid Input. Try Again")