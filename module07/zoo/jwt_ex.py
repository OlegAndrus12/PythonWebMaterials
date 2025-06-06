from jose import jwt

secret = "SHA256:DbDsphD+vFjRXtiDBmo92ifpY52ehnvz8M2Wpn71M3s"
payload = {"password": "asdasdasd23!@1"}

token = jwt.encode(payload, secret)
print(token)

payload = jwt.decode(token, secret)
print(payload)