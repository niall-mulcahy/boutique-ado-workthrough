import os
from os import path

if path.exists('../env.py'):
    import env

public_key = os.environ.get('STRIPE_PUBLIC_KEY')
print(public_key)
print(1)

secret_key = os.environ.get("STRIPE_SECRET_KEY")
print(secret_key)
print(2)

wh_key = os.environ.get("STRIPE_WH_SECRET")
print(wh_key)
print(3)

secret_message = os.environ.get("SECRET_MESSAGE")
print(secret_message)
print(4)
