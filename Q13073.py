"""
문제
You are to write a program to compute different sums based on the given positive integer N.

입력
The first line of the input includes the number of test cases, 1 ≤ t ≤ 10000. Each test case appears in one line containing 1 ≤ N ≤ 10000.

출력
For each test case, print three space separated integers S1, S2, S3 in one line where

S1 : the sum of first N positive integer,
S2 : the sum of first N positive odd integer,
S3 : the sum of first N positive even integer.
"""

"""
4
1
11
111
1111

1 1 2
66 121 132
6216 12321 12432
617716 1234321 1235432
"""

for t in range(int(input())):
    N = int(input())
    
    s1 = N * (N+1) // 2
    s2 = N * N
    s3 = N * (N+1)
    
    print(s1, s2, s3)