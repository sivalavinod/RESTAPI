import requests
a=requests.get("http://127.0.0.1:8000/rest/?format=json")
print(a.text)