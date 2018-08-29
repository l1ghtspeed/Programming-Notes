# Naive approach, runtime is too slow

def solve(length, updates):
        arr = [0]*length
        for i in updates:
                for k in range(i[0], i[1]+1):
                        arr[k] += i[2]
        return arr

# Fast approach
def solveFast(length, updates):
        arr = [0]*length
        for item in updates:
                arr[item[0]] += item[2]
                if item[1] + 1 < length:
                        arr[item[1]+1] -= item[2]
        for i in range(1, len(arr)):
                arr[i] = arr[i] + arr[i-1]
        return arr