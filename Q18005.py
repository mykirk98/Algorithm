"""
문제
Your friend has secretly picked n consecutive positive integers between 1 and 1018 and wants you to guess if their sum is even or odd.

If the sum must be even, write 2. If the sum must be odd, write 1. If the sum could be even or could be odd, write 0.

입력
The single line of input contains a single integer n (1 ≤ n ≤ 109).

출력
Output 2 if the sum of any n consecutive integers in the range from 1 to 1018 must be even, 1 if the sum must be odd, or 0 if the sum could be either even or odd.
"""

n = int(input())

if n % 4 == 0:
    print(2)
elif n % 4 == 2:
    print(1)
else:
    print(0)