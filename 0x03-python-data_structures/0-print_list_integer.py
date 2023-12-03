#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print all integers of a list, one integer per line."""
    for num in my_list:
        print("{}".format(num))

if __name__ == "__main__":
    my_numbers = [1, 2, 3, 4, 5]
    print_list_integer(my_numbers)

