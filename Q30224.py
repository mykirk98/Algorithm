"""
문제
Fact or Fiction, some people consider 7 to be a lucky digit/number.

Given a number, determine how lucky the number is by printing one of four values:

Print 0 if the number does not contain 7 and is not divisible by 7.
Print 1 if the number does not contain 7 but is divisible by 7.
Print 2 if the number does contain 7 but is not divisible by 7.
Print 3 if the number does contain 7 and is divisible by 7.
입력
There is only one input line; it contains an integer between 1 and 109, inclusive.

출력
Print one of the four messages as described above.
"""

N = int(input())

if '7' not in str(N):
    if N % 7 != 0:
        print(0)
    else:
        print(1)
else:
    if N % 7 != 0:
        print(2)
    else:
        print(3)