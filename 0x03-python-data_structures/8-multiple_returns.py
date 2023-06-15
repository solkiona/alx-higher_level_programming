#!/usr/bin/python3
def multiple_returns(sentence):
    a1 = len(sentence)
    a2 = sentence[0]

    if a1 != 0:
        new_tuple = (a1, a2)
    else:
        new_tuple = (a1, None)

    return new_tuple
