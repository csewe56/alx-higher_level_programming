#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        result_tuple = (0, None)
    else:
        first_char = sentence[0]
        result_tuple = (x, first_char)

    return result_tuple
