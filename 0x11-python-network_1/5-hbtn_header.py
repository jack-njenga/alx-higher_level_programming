#!/usr/bin/python3
"""
takes in a URL, sends a request and displays the value
of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":
    import sys, requests

    with requests.get(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id", None))
