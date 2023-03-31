import requests

url = 'http://127.0.0.1:8000/accounts/api/blog-posts/'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMjY5MTAxLCJpYXQiOjE2ODAyNTYzNDEsImp0aSI6IjRiMDZiNDRmZmQwYzQ1ZGNiOGNiNzU0OTNmNjY4ODY3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhbmphbiJ9.jtb4nUiRcuZrSASHCzt9zOtAuMHNRIFD0lxHfZ604U0'

headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.json())