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
