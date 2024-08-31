"""
문제
자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

출력
입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.
"""

import sys

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

# n = int(input())
n = int(sys.stdin.readline())
# numbers = list(map(int, input().split()))
numbers = list(map(int, sys.stdin.readline().split()))

gcd = GCD(a=numbers[0], b=GCD(a=numbers[1], b=numbers[-1]))

for g in range(1, gcd // 2 + 1):
    if gcd % g == 0:
        print(g)
print(gcd)


# for g in range(1, gcd+1):
#     if gcd % g == 0:
#         print(g)



# commonDivisor = []
# for i in range(1, int(gcd ** 0.5)):
#     if gcd % i == 0:
#         commonDivisor.append(i)
#         commonDivisor.append(gcd // i)

# if gcd ** 0.5 % 1 == 0:
#     commonDivisor.append(int(gcd ** 0.5))

# commonDivisor.sort()

# for cd in commonDivisor:
#     print(cd)