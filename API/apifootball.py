import requests

import API.APIkeys as APIkeys
import json


def make_api(url: str, params: dict = None, headers: dict = APIkeys.headers) -> json:
    url = url
    response = requests.get(url, headers=headers, params=params)
    return response.json()
