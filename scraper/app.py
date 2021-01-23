import requests
import json
import os
from dotenv import load_dotenv

from requests.exceptions import HTTPError

load_dotenv()

UN = os.getenv('USER')
PW = os.getenv('PASSWORD')
TOKEN = os.getenv('TOKEN')


url = "https://app.envoy.com/a/auth/v0/token"
payload = {"username": UN,
           "password": PW,
           "scope": "public,token.refresh",
           "grant_type": "password"}


headers = {"Authorization": "Basic " + TOKEN}
try:
    res = requests.post(url, headers=headers, data=payload)
    r = res.text
    data = json.loads(r)
    print(data['access_token'])
except Exception as err:
    print(f'Error has occurred: {err}')
