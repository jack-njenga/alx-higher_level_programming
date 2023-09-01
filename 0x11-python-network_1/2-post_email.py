#!/usr/bin/python3
"""
Takes url and email, sends a POST request with email
as parameter and displays the body
"""

if __name__ == "__main__":
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    import sys

    data = urlencode({"email": sys.argv[2]}).encode("utf-8")
    req = Request(sys.argv[1], data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
