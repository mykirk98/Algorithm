"""
문제
양의 정수 N과, N보다 큰 소수 P가 주어질 때, N!을 P로 나눈 나머지를 구하여라.

입력
첫째 줄에 N과 P가 공백으로 구분되어 주어진다.

출력
N!을 P로 나눈 나머지를 구하여라.
"""

N, P = map(int, input().split())

result = 1
for i in range(2, N+1):
    result = result * i % P

print(result % P)