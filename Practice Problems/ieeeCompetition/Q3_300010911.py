
# Rename file to Q3_<your student number>
# A is a string
# B is a string
def special(A, B):
    d = {}
    if len(A) == len(B):
        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = B[i]
            else:
                if B[i] != d[A[i]]:
                    return False
    else:
        return False

    return True


