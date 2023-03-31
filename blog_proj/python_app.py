import requests

url = 'http://127.0.0.1:8000/blog/api'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMjY0MDI3LCJpYXQiOjE2ODAyNTYzNDEsImp0aSI6ImNmOWRkMWZlODkyYjQ4ZWZiODE2NjA4MGRmMjdhNTFlIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhbmphbiJ9.-EOhUlxZOyAc2u3MszzBpaywTy-TBhkTp_9hQ0xj92c'

headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.json())