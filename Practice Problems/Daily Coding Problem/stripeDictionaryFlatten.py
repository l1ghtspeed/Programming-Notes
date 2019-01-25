'''
Problem Description:

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

def solve(d, prePend=''):
    newD = {}
    for key in d:
        if type(d[key]) is dict:
            newD.update(solve(d[key], prePend+key+'.'))
        else:
            newD[prePend+key] = d[key]
    return newD

a = {"key": 3, "foo": {"a": 5, "b": 3, "baz": {"bar": '2'}}}

print(solve(a))