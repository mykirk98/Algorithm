"""이항 계수 1"""
N, K = map(int, input().split())

N_result, K_result = 1, 1

for i in range(K):
    N_result *= N
    N -= 1
    
    K_result *= K
    K -= 1

print(int(N_result / K_result))