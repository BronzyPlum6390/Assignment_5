'''
Write a Python program that shows multiples of 2 and multiples of 3. Your program takes an
integer n as an input from a user and shows the multiples of 2 and multiples of 3 from 1 to n.
Your program should work as the following example. (⏎ represents a ‘Enter’ key stroke from a
user).


'''

def print_multiples(n):
    for i in range(1, n+1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)

n = int(input())
print_multiples(n)
