#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not isinstance(a_dictionary, dict):
        return None

    max_key = max(a_dictionary, key=a_dictionary.get, default=None)
    return (max_key)

