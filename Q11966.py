"""
문제
자연수 N이 주어졌을 때, 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 230)이 주어진다.

출력
N이 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.
"""

N = int(input())
square_of_2 = 1
while True:
    if square_of_2 == N:
        print(1)
        break
    elif square_of_2 < N:
        square_of_2 *= 2
    else:
        print(0)
        break