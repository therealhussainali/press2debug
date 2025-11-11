import os
import lesson2
import requests


# BACKEND

def Signin(enteredusername, enteredpassword):
    url = "http://127.0.0.1:5000/api/users/login"
    username = enteredusername
    passw = enteredpassword

    payload = {
        "username": username,
        "password": passw
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return "Successful Login"
    else:
        return "Invalid Login Details"


def Signup(enteredusername, enteredpassword):
    url = "http://127.0.0.1:5000/api/users/signup"
    username = enteredusername
    passw = enteredpassword

    payload = {
        "username": username,
        "password": passw
    }

    response = requests.post(url, json=payload)

    if response.status_code == 201:
        return "Successful Signup"


def fetch_todos(user_id):
    url = f"http://127.0.0.1:5000/api/users/{user_id}/todos"
    response = requests.get(url)
    todos = []

    if response.status_code == 200:
        data = response.json()
        for todo in data["todos"]:
            todos.append(todo)
        return todos
    else:
        print("Error:", response.status_code, response.text)
        return []


def add_todo(username, todo_text):
    url = "http://127.0.0.1:5000/api/users/todo"
    payload = {
        "username": username,
        "todo": todo_text
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return "Todo added successfully"
    else:
        print("Error:", response.status_code, response.text)
        return "Failed to add todo"

    