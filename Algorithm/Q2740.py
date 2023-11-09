"""행렬 곱셈
inner product(dot product) 내적은 3중 루프 반복문이라는 것을 명심할 것!
"""
N, M = map(int, input().split())
A = []
for n in range(N):
    A.append( list( map( int, input().split() ) ) )

M, K = map(int, input().split())
B =[]
for m in range(M):
    B.append( list( map( int, input().split() ) ) )

C = [[0 for j in range(K)] for i in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for n in range(N):
    for k in range(K):
        print(C[n][k], end=' ')
    print()