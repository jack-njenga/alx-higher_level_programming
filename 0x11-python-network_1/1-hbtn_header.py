#!/usr/bin/python3
"""
Takes in a url sends a request and displays the
value of the X-Request-Id variable found in the
header of the response.
"""

if __name__ == "__main__":
    import sys
    from urllib.request import urlopen

    with urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
