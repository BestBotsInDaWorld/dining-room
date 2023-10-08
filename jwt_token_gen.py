import jwt

payload = {"login": "Maksim",
           "password": "123456789"}

token = jwt.encode(payload, "sberbank",  algorithm="HS256")

print(token)