def boolean_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]  # 결과 행렬 초기화

    for i in range(n):
        for j in range(n):
            # 부울곱 연산 수행
            for k in range(n):
                C[i][j] |= A[i][k] & B[k][j]

    return C

def count_ones(matrix):
    count = 0
    for row in matrix:
        count += sum(row)
    return count


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# C = boolean_multiply(A, B)
n = len(A)
C = [[0] * n for _ in range(n)]  # 결과 행렬 초기화

for i in range(n):
    for j in range(n):
        # 부울곱 연산 수행
        for k in range(n):
            C[i][j] |= A[i][k] & B[k][j]

# result = count_ones(C)
count = 0
for row in C:
    count += sum(row)
print(count)