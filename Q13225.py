"""
문제
Given an integer n, compute the number of divisors of n.

A divisor is an integer, d (1 <= d <= n) that evenly divides n.

Example: If n=10, divisors are: 1, 2, 5 and 10. So the result would be 4.

Example: If n=104717, divisors are 1 and 104717. This is a prime number so the number of divisors is 2.

입력
The first line contains an integer C (1 <= C <= 10) with the amount of numbers you need to process. The next C lines will contain an integer n (1 <= n < 10000) each. You have to compute the number of divisors of these values.

출력
For each integer n, print a line with the number n itself, a space and the number of divisors.
"""

for i in range(int(input())):
    n = int(input())

    counter = 0
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            if n // j != j:
                counter += 2
            else:
                counter += 1
    
    print(n, counter)