"""
문제
For this problem you will compute various running sums of values for positive integers.

입력
The first line of input contains a single integer P, (1 ≤ P ≤ 10000), which is the number of data sets that follow. Each data set should be processed identically and independently.

Each data set consists of a single line of input. It contains the data set number, K, followed by an integer N, (1 ≤ N ≤ 10000).

출력
For each data set there is one line of output. The single output line consists of the data set number, K, followed by a single space followed by three space separated integers S1, S2 and S3 such that:

S1 = The sum of the first N positive integers.
S2 = The sum of the first N odd integers.
S3 = The sum of the first N even integers.
"""

for P in range(int(input())):
    K, N = map(int, input().split())
    
    S1 = N * (N + 1) // 2
    S2 = N * N
    S3 = N * (N + 1)
    print(K, S1, S2, S3)