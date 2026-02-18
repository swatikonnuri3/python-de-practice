import requests

url = "https://httpbin.org/post"
data = {"name": "Swati", "role": "Developer"}

response = requests.post(url, json=data)
print(response.json())  # server responds with the same data
