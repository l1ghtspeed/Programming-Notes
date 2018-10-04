import operator
ops = { 
    "+": operator.add, 
    "-": operator.sub, 
    "*": operator.mul, 
    "/": operator.div 
}

def solve(a):
    while len(a) > 1:
        num1 = float(a.pop())
        num2 = float(a.pop())
        operator = a.pop()
        a.append(ops[operator](num1, num2))
    return a.pop()

print(solve(["*", "3", "+", "2", "1"]))

