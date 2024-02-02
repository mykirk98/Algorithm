"""
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 NcK를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)

출력
NcK를 10,007로 나눈 나머지를 출력한다.
"""
import math

N, K = map(int, input().split())

combination= math.factorial(N) // (math.factorial(N-K) * math.factorial(K))

print(combination % 10007)