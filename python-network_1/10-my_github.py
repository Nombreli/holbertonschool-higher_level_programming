#!/usr/bin/python3
"""Uses GitHub API to get user id with Basic Auth"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    try:
        print(response.json().get("id"))
    except ValueError:
        print(None)
