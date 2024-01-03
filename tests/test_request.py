import requests
import sys

sys.path.append("./API")

import APIkeys

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"


def test_request(url: str = url):
    headers = APIkeys.headers

    response = requests.get(url, headers=headers)

    print(response.status_code)


if "__main__" == __name__:
    test_request()
