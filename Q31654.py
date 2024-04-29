"""
문제
Your friend Bob is really bad at adding numbers, and he’d like some help to make sure he’s doing it correctly! Can you help Bob make sure he is adding correctly? Given 3 integers 
$A$, 
$B$, 
$C$, make sure that 
$A + B = C$, and that Bob indeed added 
$A$ and 
$B$ correctly.

입력
The input consists of a single line with 3 integers 
$A, B, C$ where 
$-10^9 \le A, B, C \le 10^9$.

출력
Output either correct! if 
$A + B = C$, or wrong! if 
$A + B \ne C$.
"""

A, B, C = map(int, input().split())

print("correct!" if A + B == C else "wrong!")