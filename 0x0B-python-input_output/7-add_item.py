#!/usr/bin/python3
"""
Script
"""


import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

j_list = []
filename = "add_item.json"

if os.path.exists(filename):
    j_list = load_from_json_file(filename)

args = sys.argv
for arg in args:
    j_list.append(arg)

save_to_json_file(j_list, filename)
