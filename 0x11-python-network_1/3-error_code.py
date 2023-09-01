#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    import sys
    from urllib.request import urlopen 
    from urllib.error import HTTPError as herr
    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except herr as e:
        print("Error code: {}".format(e.code))
