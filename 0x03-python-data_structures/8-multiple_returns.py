#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple_s = (len(sentence), sentence[0])
    else:
        tuple_s = (0, None)
    return tuple_s
