#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        best_key = max(a_dictionary, key=a_dictionary.get, default=None)
        return best_key
    else:
        return None
