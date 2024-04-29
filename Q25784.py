"""
문제
When one looks at a set of numbers, one usually wonders if there is a relationship among them? This task is more manageable if there are only three numbers.

Given three distinct positive integers, you are to determine how one can be computed using the other two. Print 1 if any of the three numbers is the sum of the other two numbers, print 2 if any of the three numbers is the product of the other two numbers, print 3 otherwise. Assume that exactly one of these three messages will apply.

입력
There is only one input line; it contains three distinct positive integers, each between 2 and 1000 (inclusive).

출력
Print the appropriate message as described above.
"""

A, B, C = sorted(map(int, input().split()))

if A + B == C:
    print(1)
elif A * B == C:
    print(2)
else:
    print(3)