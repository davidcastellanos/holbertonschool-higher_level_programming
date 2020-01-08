#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
        except (TypeError, ValueError):
            continue
        else:
            count += 1
    print()
    return count
