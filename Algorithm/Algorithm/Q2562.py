L = []

for i in range(9):
    N = int(input())
    L.append(N)

print(max(L), L.index(max(L))+1, sep='\n')