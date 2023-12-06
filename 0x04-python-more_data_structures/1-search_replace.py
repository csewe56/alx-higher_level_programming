#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = my_list.copy()
    for i,  elem in enumerate(x):
        if elem == search:
            x[i] = replace
    return x
