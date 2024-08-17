"""
문제
모태 솔로인 세진이는 이번에는 꼭 여자친구를 사귀어야겠다는 마음으로 형진이가 주최한 미팅에 참석하게 된다. 하지만 안타깝게도 컴퓨터공학과는 남초학과이기 때문에 항상 남자의 수가 여자의 수보다 많거나 같다. 마음이 급해진 세진이는 항상 모든 여자들이 남자들과 짝을 이루어진다고 가정하였을 때 남자들이 미팅에서 여자들에게 선택되는 모든 경우를 시뮬레이션 해보려고 한다. 예를들어 남자 3명 여자 2명이 있을 때, 남자 1 남자2 가 선택되는 경우, 남자 2 남자 3이 선택되는 경우, 남자1 남자3 이 선택되는 경우로 경우의 수는 3가지가 존재한다. 세진이를 도와 미팅에서 선택될 수 있는 남자들의 모든 상태의 경우의 수를 구해보자.

단, 수가 너무 커질 수 있으니 1000000007로 나눈 나머지를 구해보자.

입력
입력의 첫째 줄에 남학생의 수 N(2 ≤ N ≤ 1000000)명 여학생의 수 M(1 ≤ M ≤ N)명이 주어진다.

출력
경우의 수를 1000000007로 나눈 나머지를 출력하라. 
"""

def combination(n, r):
    result = 1
    r = max(r, n-r)
    for i, j in enumerate(range(n, n-r, -1)):
        result *= j % 1000000007
        result /= (i+1) % 1000000007
    
    return int(result)

N, M = map(int, input().split())

print(combination(n=N, r=M) % 1000000007)

MOD = 1000000007

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def nCr_mod(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    numerator = 1
    denominator = 1
    
    for i in range(r):
        numerator = (numerator * (n - i)) % p
        denominator = (denominator * (i + 1)) % p
    
    return (numerator * mod_inverse(denominator, p)) % p

# 입력 처리
N, M = map(int, input().split())

# 결과 출력
print(nCr_mod(N, M, MOD))
