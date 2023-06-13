#!/usr/bin/python3
"""
"""


import sys, json, os.path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

j_list = []
filename = "add_item.json"

if os.path.exists(filename):
    j_list = load(filename)

args = sys.argv
for arg in args:
    j_list.append(arg)

with open(filename, "w", encoding="utf-8") as f:
    f.write(str(json.dumps(j_list)))



