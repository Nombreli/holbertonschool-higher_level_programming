#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer safely using {:d}.format()

    Args:
        value: istənilən tip ola bilər (int, str, və s.)

    Returns:
        True: əgər integer düzgün çap olunubsa
        False: əks halda
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
