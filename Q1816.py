"""
문제
현대 사회에서 통용되고 있는 많은 종류의 암호 시스템에서는, 매우 큰 소수의 곱으로 만들어진 수를 암호 키로 이용하는 경우가 많다. 현실적으로 매우 큰 수를 빠른 시간 내에 소인수분해하는 것은 어려운 일이기 때문이다.

물론 실제 생활에서는 수십만 또는 수백만 자리 이상의 매우 큰 소수가 활용되지만 그러한 소수를 구하는 것은 매우 어려운 일이므로, 우리는 좀 더 스케일이 작은 경우에 대해서만 생각해 보기로 하자. 1,000,000=106보다 큰 소수이면 매우 큰 소수로 생각하는 것이다.

어떤 수 S가 주어지면, 이 수가 우리가 생각하는 스케일이 작은 경우에서 적절한 암호 키인지 아닌지를 구하는 프로그램을 작성하시오. 만일 S의 모든 소인수가 106보다 크다면 그 수는 적절한 암호 키이고, 그렇지 않은 경우는 적절하지 못한 암호 키가 된다.

입력
첫째 줄에는 수의 개수 N ()이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 확인하고자 하는 수 S가 한 줄에 하나씩 주어진다.

출력
N개의 줄에 걸쳐, 입력받은 수가 적절한 암호 키이면 YES, 아니면 NO를 순서대로 출력한다.
"""

for N in range(int(input())):
    S = int(input())

    for i in range(2, 1000001):
        if S % i == 0:
            print('NO')
            break
        
        if i == 1000000:
            print('YES')