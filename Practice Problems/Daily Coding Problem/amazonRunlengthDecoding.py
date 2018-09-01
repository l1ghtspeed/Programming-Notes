def solve(s):
    count = 0
    newS = '1'
    rev = s[::-1]
    for char in rev:
        if newS[-1] == char:
            count += 1
        else:
            newS += str(count)
            newS += char
            count = 1

    newS += str(count)
    return newS[:1:-1]

print(solve('hello'))

