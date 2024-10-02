"""
문제
Dima is bored of playing checkers with himself. Since there is nothing but checker pieces to play with, he came up with the following game.

Each piece he has is either white or black. Dima builds a tower by stacking his pieces on top of each other in some order. A black stripe is a sequence of adjacent black pieces, with either a white piece, or the end of the tower at the bottom and top of it. In other words, two adjacent black pieces always belong to the same black stripe. The goal of the game is to get the maximum number of black stripes in the tower.

The game has just started. Dima has 
$a$ white and 
$b$ black pieces. What is the maximum number of black stripes he can get in his tower?

입력
The only line of input contains two integers 
$a$ and 
$b$ --- the number of white and black pieces, respectively (
$0 \le a, b \le 10^{18}$).

출력
Output a single integer --- the maximum possible number of black stripes.
"""

a, b = map(int, input().split())

if a >= b:
    print(b)
elif a + 1 <= b:
    print(a + 1)
elif a == 0:
    print(1)
elif b == 0:
    print(0)