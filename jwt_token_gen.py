# import pyjwt
import jwt

payload = {"login": "Admin",
           "password": "123456789"}

token = jwt.encode(payload, "sberbank",  algorithm="HS256")

print(token)