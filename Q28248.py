"""
문제
In the game, Deliv-e-droid, a robot droid has to deliver packages while avoiding obstacles. At the end of the game, the final score is calculated based on the following point system:

Gain 
$50$ points for every package delivered.
Lose 
$10$ points for every collision with an obstacle.
Earn a bonus 
$500$ points if the number of packages delivered is greater than the number of collisions with obstacles.
Your job is to determine the final score at the end of a game.

입력
The input will consist of two lines. The first line will contain a non-negative integer 
$P$, representing the number of packages delivered. The second line will contain a non-negative integer 
$C$, representing the number of collisions with obstacles.

출력
The output will consist of a single integer 
$F$, representing the final score.
"""

P = int(input())
C = int(input())

print(P * 50 - C * 10 + (500 if P > C else 0))