"""
문제
Farmer John was performing his nightly bedtime reading duties for Bessie. "Oh, this gives me a headache," moaned Bessie. "But it's just simple number theory," replied FJ. "Let's go over it again. The sigma function of a number is just the sum of the divisors of the number. So, for a number like 12, the divisors are 1, 2, 3, 4, 6, and 12. Summing them we get 28." "That's all there is to it?" asked Bessie. "Yep." replied FJ. "Perhaps someone will write a program to calculate the sigma function of an integer I (1 <= I <= 1,000,000)."

입력
A single integer I.

출력
Output a line containing the sum of all of I's divisors.
"""

I = int(input())

sum_divisors = 0
for i in range(1, int(I ** 0.5) + 1):
    if I % i == 0:
        if I // i == i:
            sum_divisors += i
        else:
            sum_divisors += i + I // i

print(sum_divisors)