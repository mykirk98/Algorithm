"""
문제
The impossible has happened. Bear G. has fallen into his own trap. Lured by a delicious box of Domaćica, without even thinking, he rushed and fell into his trap. In order to get out of the trap, he must solve the following task with your help. You are given three integers L, D i X.

determine the minimal integer N such that L ≤ N ≤ D and the sum of its digits is X
determine the maximal integer M such that L ≤ M ≤ D and the sum of its digits is X
Bear will be able to escape from the trap if he correctly determines numbers N and M. The numbers N and M will always exist.

입력
The first line of input contains the integer L (1 ≤ L ≤ 10 000), the number from the task.

The second line of input contains the integer D (1 ≤ D ≤ 10 000, L ≤ D), the number from the task.

The third line of input contains the integer X (1 ≤ X ≤ 36), the number from the task.

출력
The first line of output must contain the integer N from the task.

The second line of output must contain the integer M from the task
"""

L = int(input())
D = int(input())
X = int(input())

satisfied = []
for i in range(L, D+1):
    i = str(i)
    total = 0
    for j in i:
        total += int(j)
    
    if total == X:
        satisfied.append(i)

print(satisfied[0])
print(satisfied[-1])