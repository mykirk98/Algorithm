"""
# 과자 한 개 가격 : K
# 과자의 개수 : N
# 현재 가진 돈의 액수 : M

# 구하고자 하는 값 : K * N - M
"""
K, N, M = map(int, input().split())

if K * N >= M:
    needs = K * N - M
else:
    needs = 0

print(needs)