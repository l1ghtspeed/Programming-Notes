'''
Google Code Jam 2019 Qualifiers Question 1: Foregone Solution
Problem:

Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out an oversized check, we encountered a problem.
The value of N, which is an integer, includes at least one digit that is a 4... and the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, 
such that neither A nor B contains any digit that is a 4, and A + B = N.
Please help us find any pair of values A and B that satisfy these conditions.
'''

t = int(input())
for testcase in range(t):
    N = input()
    a = ''
    b = ''
    for num in N:
        if num == '4':
            a+='3'
            b+='1'
        else:
            a+=num
            b+='0'
    print("Case #" + str(testcase+1) + ": " + a + " " + str(int(b)))