import requests
url = "http://127.0.0.1:5000/api/add"
urlhello = "http://127.0.0.1:5000/api/hello"


payload = {
    "num1": 5,
    "num2": 10
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())

response = requests.get(urlhello)
print(response.json())