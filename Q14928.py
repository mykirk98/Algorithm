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
"""

N = int(input())

result = N % 20000303

print(result)