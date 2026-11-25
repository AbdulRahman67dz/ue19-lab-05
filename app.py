import requests

r = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
print(r.json()["joke"])
