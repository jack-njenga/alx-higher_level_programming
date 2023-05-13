#!/usr/python3

def multiple_returns(sentence):
    if sentence is None:
        return tuple([0, 'None'])

    ret = [len(sentence), sentence[0]]
    return tuple(ret)
