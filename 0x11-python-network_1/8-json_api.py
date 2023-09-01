#!/usr/bin/python3
"""
Search API
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = argv[1]
    else:
        q = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        res_dict = response.json()
        id, name = res_dict.get("id"), res_dict.get("name")
        if len(res_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(res_dict.get('id'), res_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
