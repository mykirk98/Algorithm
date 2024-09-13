"""
문제
두 정수 n과 m이 주어졌을 때, 0 < a < b < n인 정수 쌍 (a, b) 중에서 (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, n과 m이 주어진다. 두 수는 0보다 크고, 100보다 작거나 같다.

출력
각 테스트 케이스마다 문제의 조건을 만족하는 (a, b)쌍의 개수를 출력한다.
"""

from sys import stdin

for T in range(int(stdin.readline())):
    n, m =map(int, stdin.readline().split())

    count = 0

    # for a in range(1, n+1):
    #     for b in range(a+1, n):
    #         if ((a ** 2 + b ** 2 + m) / (a * b)) % 1 == 0:
    #             count += 1

    # print(count)


    for b in range(2, n):
        for a in range(1, b):
            if ((a ** 2 + b ** 2 + m) / (a * b)) % 1 == 0:
                count += 1

    print(count)