N, M = map(int, input().split())

basket = [0 for n in range(N)]

for m in range(M):
    i, j, k = map(int, input().split())

    for a in range(j-i+1):
        basket[i-1+a] = k

for i in range(N):
    print(basket[i], end=' ')