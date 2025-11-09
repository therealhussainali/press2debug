import requests
url = "http://127.0.0.1:5000/api/users"

payload = {
    "username": "hussain ali",
    "email": "testemail@gmail.com",
    "password": "1234"
}

response = requests.post(url, json=payload)

print(response.status_code)