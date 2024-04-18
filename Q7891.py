"""
문제
Given two integers, calculate and output their sum.

입력
The input contains several test cases. The first line contains and integer t (t ≤ 100) denoting the number of test cases. Then t tests follow, each of them consisiting of two space separated integers x and y (−109 ≤ x, y ≤ 109).

출력
For each test case output output the sum of the corresponding integers.
"""

for t in range(int(input())):
    A, B = map(int, input().split())
    print(A + B)