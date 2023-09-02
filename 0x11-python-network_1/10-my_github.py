#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    from requests import get

    response = get("https://api.github.com/user",
                   auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
