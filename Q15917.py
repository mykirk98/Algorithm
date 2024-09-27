"""
문제
여러분은 Q개의 쿼리를 수행해야 합니다. 수행해야 하는 쿼리는 다음과 같습니다.

어떤 수 a를 2의 거듭제곱 꼴로 나타낼 수 있는가?

입력
첫 줄에 Q가 주어집니다. (1 ≤ Q ≤ 106)

두 번째 줄부터 Q+1번째 줄까지 a가 주어집니다. a는 1이상 231-1이하 자연수입니다.

출력
각 쿼리마다, 답이 Yes이면 1을, 그렇지 않으면 0을 출력합니다.
"""

import sys
input = sys.stdin.readline

for Q in range(int(input())):
    a = int(input())

    binary_a = bin(a)[2:]

    if binary_a.count('1') == 1:
        print(1)
    else:
        print(0)