#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Bütün dəyərləri 2-yə vurulmuş yeni lüğət qaytarır."""
    return {key: value * 2 for key, value in a_dictionary.items()}
