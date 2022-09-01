#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bestScore = 0
    bestKey = None
    for name, value in a_dictionary.items():
        if value > bestScore:
            bestScore = value
            bestKey = name
    return bestKey
