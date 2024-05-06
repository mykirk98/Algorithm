"""
문제
You have a rectangular field you want to plant with corn. You know the dimensions of the field in yards, and you know that one bag of corn seed will cover 5 acres. Having passed all your elementary math courses you also know that 4840 square yards is equal to 1 acre. So, given the dimensions of the rectangular field in yards you must compute the number of bags of corn seed you need to plant the entire field.

입력
The first line contains two positive integers that are the dimensions of the rectangular field in yards.

출력
A positive integer that is the number of bags of corn seed needed to plant the entire field.
"""

from math import ceil

x, y = map(int, input().split())

print(ceil(x * y / (4840 * 5)))