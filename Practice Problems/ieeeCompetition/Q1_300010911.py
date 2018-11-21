
# Rename file to Q1_<your student number>
# A is a list of integers
# d is the number of elements to rotate by
def rot(A, d):
    l = len(A)
    newA = [0]*l
    for i in range(l):
        newA[(i-d%l)] = A[i]
    return newA

print(rot([], 1))

    
