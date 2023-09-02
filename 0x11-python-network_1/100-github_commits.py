#!/usr/bin/python3
"""
takes 2 arguments, and lists 10 commits of a repo
"""

if __name__ == "__main__":
    import requests
    import sys

    res = requests.get("https://api.github.com/repos/{}/{}/commits".
                       format(sys.argv[1], sys.argv[2]))

    content = res.json()
    for commit in content[:10]:
        print(commit.get("sha"), end=": ")
        print(commit .get("commit").get("author").get("name"))
