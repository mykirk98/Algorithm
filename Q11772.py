"""
문제
The teacher has sent an e-mail to her students with the following task:

"Write a programme that will determine and output the value of 
\(X\) if given the statement:

 
\[X = number_1^{pot_1} + number_2^{pot_2} + \dots + number_N^{pot_N}\] 

and it holds that 
\(number_1\), 
\(number_2\) to 
\(number_N\) are integers, and 
\(pot_1\), 
\(pot_2\) to 
\(pot_N\) one-digit integers." Unfortunately, when the teacher downloaded the task to her computer, the text formatting was lost so the task transformed into a sum of 
\(N\) integers:

 
\[X = P_1 + P_2 + ... + P_N\] 

For example, without text formatting, the original task in the form of 
\(X = 21^2 + 125^3\) became a task in the form of 
\(X = 212 + 1253\). Help the teacher by writing a programme that will, for given 
\(N\) integers from 
\(P_1\) to 
\(P_N\) determine and output the value of 
\(X\) from the original task.

Please note: We know that it holds a 
\(N = a \cdot a \cdot \dots \cdot a\) (
\(N\) times).

입력
The first line of input contains the integer 
\(N\) (1 ≤ 
\(N\) ≤ 10), the number of the addends from the task. Each of the following 
\(N\) lines contains the integer 
\(P_i\) (10 ≤ 
\(P_i\) ≤ 9999, 
\(i\) = 1 ... 
\(N\)) from the task.

출력
The first and only line of output must contain the value of 
\(X\) (
\(X\) ≤ 1 000 000 000) from the original task.
"""

X = 0
for N in range(int(input())):
    P = input()
    X += int(P[:-1]) ** int(P[-1])

print(X)