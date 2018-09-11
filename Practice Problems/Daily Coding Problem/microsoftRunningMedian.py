# Brute Force Method
import math
def solve(a):
    for i in range(len(a)):
        temp = sorted(a[0:i+1])
        if len(temp)%2 == 0:
            print((temp[math.floor(i/2)]+temp[math.ceil(i/2)])/2)
        else:
            print(temp[int(i/2)])

solve([2, 1, 5, 7, 2, 0, 5])

# Efficient Method