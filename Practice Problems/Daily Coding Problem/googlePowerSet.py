'''
Problem:

Given a set S, return the power set of set S

'''

def power_set(s):
    if not s:
        return [[]]
    result = power_set(s[1:])
    return result + [subset + [s[0]] for subset in result]