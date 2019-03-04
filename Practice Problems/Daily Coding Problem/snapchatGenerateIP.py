'''

Problem Description:

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].

'''


def generate_IP_addresses(s, parts=[]):
    addresses = []

    if len(parts) > 4:
        return []

    if not s:
        if len(parts) == 4:
            return [".".join(parts)]
        else:
            return []

    addresses += generate_IP_addresses(s[1:], parts + [s[:1]])

    if len(s) > 1 and 10 <= int(s[:2]) <= 99:
        addresses += generate_IP_addresses(s[2:], parts + [s[:2]])

    if len(s) > 2 and 100 <= int(s[:3]) <= 255:
        addresses += generate_IP_addresses(s[3:], parts + [s[:3]])

    return addresses