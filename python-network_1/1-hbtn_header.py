#!/usr/bin/python3
"""Gets X-Request-Id header from response"""

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
