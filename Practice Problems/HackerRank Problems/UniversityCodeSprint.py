def speedLimites(s):
    n = int(s)
    if n <= 90:
        print('0 No punishment')
    elif n <= 110:
        print(str((n-90)*300)+ ' Warning')
    else:
        print(str((n-90)*500)+ ' License removed')