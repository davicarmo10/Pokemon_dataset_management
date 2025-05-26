import requests

url = "http://127.0.0.1:8000/recomendar/"
data = {
    "name": "Pikachu",
    "top_n": 5
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Resposta da API:", response.json())
