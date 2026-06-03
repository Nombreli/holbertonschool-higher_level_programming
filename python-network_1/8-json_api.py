#!/usr/bin/python3
"""Search API with JSON response handling"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {"q": q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
        exit()

    if not result:
        print("No result")
    else:
        print("[{}] {}".format(result.get("id"), result.get("name")))
