'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def solve(m):
    if len(m) >= 2:
        if m[0]*10 + m[1] < 27:
            return  solve(m[2:]) + solve(m[1:])
        else:
            return solve(m[1:])
    else:
        return 1

print(solve([1, 1, 1]))