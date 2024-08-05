"""
문제
정수 M개가 주어졌을 때, 모든 두 수의 쌍 중에서 가장 큰 최대공약수 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 N (1 < N < 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 양의 정수 M (1 < M < 100)개가 주어진다. 모든 수는 -231보다 크거나 같고, 231 -1보다 작거나 같다. 

출력
각 테스트 케이스마다, 입력으로 주어진 수의 모든 두 수의 쌍의 최대공약수 중 가장 큰 값을 출력한다.
"""

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    
    return a

for N in range(int(input())):
    M = list(map(int, input().split()))

    max_GCD = 0
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            if GCD(M[i], M[j]) > max_GCD:
                max_GCD = GCD(M[i], M[j])

    print(max_GCD)