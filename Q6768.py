"""
문제
A CCC soccer game operates under slightly different soccer rules. A goal is only counted if the 4 players, in order, who touched the ball prior to the goal have jersey numbers that are in strictly increasing numeric order with the highest number being the goal scorer.

Players have jerseys numbered from 1 to 99 (and each jersey number is worn by exactly one player).

Given a jersey number of the goal scorer, indicate how many possible combinations of players can produce a valid goal.

입력
The input will be the positive integer J (1 ≤ J ≤ 99), which is the jersey number of the goal scorer.

출력
The output will be one line containing the number of possible scoring combinations that could have J as the goal scoring jersey number.
"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

J = int(input())
if J == 4:
    print(1)
elif J < 4:
    print(0)
else:
    print(combination(n=J-1, r=3))