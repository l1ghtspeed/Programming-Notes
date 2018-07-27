# Normal recursive function
n = 40

def fib_recursive(n):
    if (n == 1) or (n ==2):
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

#print(fib_recursive(n))

# Recursion with memoization
def fib_memoize(n, memo):
    if (memo[n]):
        return memo[n]
    else:
        if (n == 1) or (n == 2):
            memo[n] = 1
            return 1
        else:
            memo[n] = fib_memoize(n-1, memo) + fib_memoize(n-2, memo) 
            return memo[n]
    

print(fib_memoize(n, [0]*(n+1)))


# Using a for loop

def fib_loop(n):
    s1 = 1
    s2 = 1
    for i in range(2, n):
        temp = s2
        s2 = s2 + s1
        s1 = temp

    return s2

print(fib_loop(n))
