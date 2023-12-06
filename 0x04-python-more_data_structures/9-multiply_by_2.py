#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = {j: a_dictionary[j] * 2 for j in a_dictionary}
    return k
