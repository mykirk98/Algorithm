"""
문제
양의 정수 N이 주어졌을 때, 이 수를 소인수분해 한 결과를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 수가 주어진다. 각 테스트 케이스마다 양의 정수 N (2 ≤ N ≤ 100,000)이 주어진다.

출력
각 테스트 케이스마다 각 인수와 그 인수가 곱해진 횟수를 한 줄씩 출력한다. 출력 순서는 인수가 증가하는 순으로 한다.
"""

for T in range(int(input())):
    N = int(input())

    history = {}
    div = 2
    while N != 1:
        if N % div == 0:
            if div not in history:
                history[div] = 1
            else:
                history[div] += 1
            N //= div
        else:
            div += 1

    for k, v in history.items():
        print(k, v)