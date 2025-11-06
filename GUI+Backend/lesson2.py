import hashlib
import os
import login
import signup

# Hashing
# Functions
# repeated code is less
# cleaner efficient

# Module Login
# Module Signup 
# Module Hashing

def hash_password(password):
    # Create a SHA256 hash of the password
    return hashlib.sha256(password.encode()).hexdigest()


# testpassw = input("Enter Password: ")
# hashedpassw = hash_password(testpassw)
# print(hashedpassw) 
# 27cc6994fc1c01ce6659c6bddca9b69c4c6a9418065e612c69d110b3f7b11f8a (hello123)
# a727e78178127dfce8ba145cd64b7929a30fac28c7e81340761efea1c59aee09 (hello12)


def main():
    # Entry Point
    print("Welcome! Do you want to login or sign up?")

    while (True):
        choice = input("Type 'login' or 'signup':").lower()
        if (choice == "login"):
            login.Signin()
        elif (choice == "signup"):
            signup.Register()
        else:
            print("Invalid choice, please enter again")



if __name__ == "__main__":
    main()

