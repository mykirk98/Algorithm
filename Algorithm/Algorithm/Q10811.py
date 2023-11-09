from math import ceil

N, M = map(int, input().split())
basket = [n for n in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())

    for k in range(ceil(abs(j-i)/2)):
        temp = basket[i-1+k]
        basket[i-1+k] = basket[j-1-k]
        basket[j-1-k] = temp

result = ' '.join(map(str, basket))
print(result)