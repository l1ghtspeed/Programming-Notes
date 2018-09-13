def isPowof2(a):
    while a > 2:
        temp = bin(a)
        if temp[-1] == '1':
            return False
        else:
            a = a>>1
    return True

def s():
    for i in range(17):
        print(isPowof2(i))
s()
