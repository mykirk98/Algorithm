"""
문제
세 정수 A, B, C의 평균은 (A+B+C)/3이다. 세 정수의 중앙값은 수의 크기가 증가하는 순서로 정렬했을 때, 가운데 있는 값이다.

두 정수 A와 B가 주어진다. 이때, A, B, C의 평균과 중앙값을 같게 만드는 가장 작은 정수 C를 찾는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, A와 B가 주어진다. (1 ≤ A ≤ B ≤ 109) 입력의 마지막 줄에는 0이 두 개 주어진다. 

출력
각 테스트 케이스에 대한 정답을 한 줄에 하나씩 출력한다.
"""

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    # gap = B - A
    # C = A - gap
    # A - (B - A)
    C = 2 * A - B
    print(C)