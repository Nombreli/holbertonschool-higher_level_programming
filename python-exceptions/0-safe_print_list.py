#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # siyahının sonuna çatanda səhv çıxır, onu tuturuq
        pass
    print()  # yeni sətir
    return count
