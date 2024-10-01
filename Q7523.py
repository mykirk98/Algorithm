"""
문제
카를 프리드리히 가우스는 독일의 수학자이다.

가우스가 초등학교에 다닐 때, 선생님 J.G. Büttner는 1부터 100까지 수의 합을 계산하게 시켰다. 가우스는 몇 초만에 정확한 답 5050을 계산했다.

n과 m 이 주어졌을 때, n보다 크거나 같고, m보다 작거나 같은 모든 정수의 합을 구하는 프로그램을 작성하시오. 즉, 다음을 계산하라.

 
\[\sum_{i=n}^{m} {i} = n+(n+1)+(n+2)+ \dots + (m-1) + m\] 

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, n과 m이 주어진다. (-109 ≤ n ≤ m ≤ 109)

출력
각 테스트 케이스마다 "Scenario #i:"를 출력한 다음, n부터 m까지 모든 정수의 합을 출력한다. 각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.
"""

for i, T in enumerate(range(int(input()))):
    n, m = map(int, input().split())

    length = m - n + 1

    if length % 2 == 0:
        pivot = length // 2
        total = (n + m) * pivot
    else:
        pivot = length // 2
        total = (n + m) * pivot + (n + m) // 2

    print(f'Scenario #{i+1}:')
    print(total)
    print()