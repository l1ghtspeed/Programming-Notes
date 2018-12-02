'''
Problem Description:

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

'''

def solve(s):
    s = s.split()
    s = ' '.join(s[::-1])
    return s

print(solve("hello world"))
    