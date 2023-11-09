def factorial(n):       # failed 2 time
    if n == 0:
        return 1
    
    return n * factorial(n-1)

N = int(input())

print(factorial(N))