"""
문제
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

출력
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
"""

# import math

# T = int(input())

# for t in range(T):
#     A, B = map(int, input().split())

#     divisor_A, divisor_B = [], []

#     # A의 약수 구하기
#     for a in range(1, int(math.sqrt(A) + 1)):
#         if A % a == 0:
#             divisor_A.append(a)
#             divisor_A.append(int(A / a))

#     # B의 약수 구하기
#     for b in range(1, int(math.sqrt(B) + 1)):
#         if B % b == 0:
#             divisor_B.append(b)
#             divisor_B.append(int(B / b))

#     # 공약수 구하기
#     commonDivisor = 0
#     for a in divisor_A:
#         for b in divisor_B:
#             if a == b:
#                 commonDivisor = a

#     print(A * B // commonDivisor)

def EuclideanAlgorithm(x, y):
    if x % y == 0:
        return y
    
    return EuclideanAlgorithm(y, x % y)

T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    GCD = EuclideanAlgorithm(x=A, y=B)
    print(A * B // GCD)