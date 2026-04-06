#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, only integers.

    Args:
        my_list (list): istənilən tip elementlər ola bilər
        x (int): baxılacaq elementlərin sayı

    Returns:
        int: həqiqətən çap olunan integer-lərin sayı
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # integer olmayanları səssizcə ötürürük
            continue
        except IndexError:
            # siyahının sonuna çatanda səhv çıxır
            raise
    print()
    return count
