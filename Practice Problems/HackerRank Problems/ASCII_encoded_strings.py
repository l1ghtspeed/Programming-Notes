# Complete the decode function below.
def decode(encoded):
    # Note that this implementation assumes that all strings are properly decodable
    proper = encoded[::-1]
    iterator = 0
    s = ''
    while iterator < len(encoded):
        num = int(proper[iterator:iterator+2])
        if num < 65:
            if num == 32:
                s += ' '
                iterator += 2
            else:
                s += chr(int(proper[iterator:iterator+3]))
                iterator += 3
        else:
            s += chr(num)
            iterator += 2
    return s
