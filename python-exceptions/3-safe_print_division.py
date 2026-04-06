#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result.

    Args:
        a (int): birinci ədəd
        b (int): ikinci ədəd

    Returns:
        float: bölmənin nəticəsi
        None: əgər bölmə mümkün deyilsə
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
