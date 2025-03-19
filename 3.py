"""

Write a Python program that takes an integer n as an input from a user and shows the return
value of the addTotal function and the gMul variable. Your program should work as the
following example. (⏎ represents a ‘Enter’ key stroke from a user).
A. addTotal function: takes an integer parameter and returns the sum of the all integers
from one to the given parameter.
B. mulTotal function: takes an integer parameter, computes the multiplication of the all
integers from one to the given parameter, and stores the multiplication result to the global
variable gMul. muTotal returns nothing.

"""


def addTotal(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

gMul = 1  

def mulTotal(n):
    global gMul
    for i in range(1, n+1):
        gMul *= i

n = int(input())
print("addTotal(): " + str(addTotal(n)))
mulTotal(n)
print("gMul: " + str(gMul))