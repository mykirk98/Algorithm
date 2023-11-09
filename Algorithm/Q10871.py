N, X = map(int, input().split())

A = list(map(int, input().split()))

for n in range(N):
    if X > A[n]:
        print(A[n], end=' ')