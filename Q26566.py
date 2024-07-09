"""
문제
There’s a pizza store which serves pizza in two sizes: either a pizza slice, with area A1 and price P1, or a circular pizza, with radius R1 and price P2. You want to maximize the amount of pizza you get per dollar. Should you pick the pizza slice or the whole pizza?

입력
The first line of input will contain a single integer n that indicates the number datasets to follow. Each dataset is comprised of two lines. The first line contains two space-separated integers A1 and P1. Similarly, the second line contains two space-separated integers R1 and P2. It is guaranteed that all values are positive integers at most 103. We furthermore guarantee that the two will not be worth the same amount of pizza per dollar.

출력
For each data set, print on a single line, either “Whole pizza” or “Slice of pizza” depending on which is the better deal.
"""

from math import pi

for n in range(int(input())):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())

    A = A1 / P1
    B = R1 * R1 * pi / P2

    if A > B:
        print("Slice of pizza")
    else:
        print("Whole pizza")