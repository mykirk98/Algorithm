"""
문제
Given an odd integer N, calculate the sum of all the odd integers between 1 and N inclusive.

입력
First line of the input contains T, the number of test cases. Each test case contains a single integer N. N is between 1 and 100.

출력
For each test case output the value 1+3+….+N.
"""

for T in range(int(input())):
    N = int(input())
    if N % 2 == 1:
        total = 0
        for i in range(1, N+1, 2):
            total += i
        print(total)