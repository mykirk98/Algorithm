"""
문제
A large coffee spill in the warehouse of the Busy Association of Papercutters on Caffeine has stained the corners of all paper in storage. In order to not waste money, it was decided that these dirty corners should be cut off of all pieces of paper.

A few members loudly proclaim that cuts should be made diagonally, while other members say that cutting the corner out as a rectangle is the better option. Both parties claim their method is better.

You decide to end this discussion once and for all, telling the rectangle-cutters that their method is slower. You set out to show them the following: given a piece of paper which has a 
$w$ by 
$h$ corner that is stained with coffee that needs to be to cut off, how much more effort is it to cut out the whole rectangle compared to cutting along the diagonal?

입력
The input consists of:

A line containing two integers 
$w$ and 
$h$ (
$1\leq w,h\leq 100$), representing the width and height of the corner respectively.
출력
Output how much longer you have to cut if you cut out a rectangle, compared to cutting along the diagonal. Your answer should have an absolute or relative error of at most 
$10^{-6}$.
"""

w, h = map(int, input().split())

print(w + h - (w ** 2 + h ** 2) ** 0.5)