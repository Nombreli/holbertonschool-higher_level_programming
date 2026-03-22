#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Lüğətdən açarı silən funksiya (açar yoxdursa, heç nə etmir)."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
