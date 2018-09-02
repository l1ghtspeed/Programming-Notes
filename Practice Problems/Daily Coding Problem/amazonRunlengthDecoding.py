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

def decode(s):
    newS = ''
    iterator = 0
    mark = -1
    while iterator in range(len(s)):
        if s[iterator].isalpha():
            if mark != iterator:
                newS += s[iterator]*int(s[mark+1:iterator])
            mark = iterator
        iterator+=1
    return newS
        
        
        

