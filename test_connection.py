from bot.client import client

try:
    account = client.futures_account()
    print(account)
except Exception as e:
    print(type(e))
    print(e)