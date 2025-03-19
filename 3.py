

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