import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

data = response.json()  # convert response to Python dict
print(data["login"])     # prints 'octocat'
print(data["public_repos"])
