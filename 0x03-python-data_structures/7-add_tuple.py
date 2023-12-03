#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_first = 0
    result_second = 0

    if len(tuple_a) >= 1:
        result_first += tuple_a[0]

    if len(tuple_a) >= 2:
        result_second += tuple_a[1]

    if len(tuple_b) >= 1:
        result_first += tuple_b[0]

    if len(tuple_b) >= 2:
        result_second += tuple_b[1]

    return (result_first, result_second)
