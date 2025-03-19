def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    return int1 / int2

def mod(int1, int2):
    return int1 % int2

def printMsg():
    print("completed")
    

n1 = int(input())
n2 = int(input())

print("sum: " + str(add(n1, n2)))
print("difference: " + str(subtract(n1, n2)))
print("product: " + str(multiply(n1, n2)))
print("division: " + str(divide(n1, n2)))
print("remainder:" + str(mod(n1, n2)))
printMsg()