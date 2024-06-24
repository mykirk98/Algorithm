"""
문제
환규는 오늘부터 주식 투자를 하려고 한다. 열심히 정보를 수집한 결과 A사, B사, C사에 투자하기로 했다. 환규는 오늘 산 주식이 내일 오를지, 떨어질지 예측하는 것이 아직은 힘들다. 그래서 다음과 같이 투자를 하기로 했다. 먼저 서로 다른 날에는 서로 다른 회사의 주식을 살 수 있지만, 하루에는 최대 1개 회사의 주식만 사도록 한다. 매일 장이 열리기 전에 A사, B사, C사 중 그날 주식을 살 회사를 하나 정한 후, 장이 열릴 때 정한 회사의 주식을 산다. 그 다음 장이 닫힐 때 그날 산 주식을 모두 판다. 만약 세 회사 중 어느 곳도 수익이 날 것 같지 않으면 주식을 구매하지 않아도 된다.

환규는 주식을 처음 해보기 때문에 과연 주식으로 돈을 벌 수 있을지 궁금해졌다. 그래서 투자하려는 회사들의 지난 N일 동안의 주식 데이터를 이용해 N일 동안 위 규칙을 지키며 주식투자를 했을 때 과연 얼마를 벌 수 있는지 계산해 보기로 했다. 먼저 A사, B사, C사의 N일 동안의 주가 데이터를 모았다. 환규는 이 데이터를 이용해 각 회사별로 장이 열릴 때 주식을 사고, 장이 닫힐 때 모두 팔았을 경우 매일 얼마를 벌 수 있었는지 정리했다. 다음은 N = 4일때 환규가 정리한 데이터를 나타내는 표이다.

날짜
회사명	1일	2일	3일	4일
A사	500	300	-100	600
B사	800	0	-200	200
C사	200	300	-400	300
위 표에서 양수는 이익을, 음수는 손해를 나타내며, 0은 이익도, 손해도 없음을 의미한다. 예를 들어 1일째에 A사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 팔면 500의 이익을 얻을 수 있었다. 만약 3일째에 C사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 판다면 400의 손해가 생겼을 것이다.

데이터를 분석하던 환규는 자신이 정리한 데이터를 이용해서 N일 동안 규칙을 지키면서 매일 최적의 투자를 할 경우 최대 얼마를 벌 수 있었는지 궁금해졌다. 예를 들어 위 표에서 1일째에는 B사의 주식을 사면 가장 많은 이익을 남길 수 있다. 2일째에는 A사, 또는 C사의 주식을 사면 가장 많은 이익을 남길 수 있다. 3일째에는 어떤 주식을 사도 손해가 나므로 주식을 사지 않는다. 4일째에는 A사의 주식을 사면 된다. 이렇게 주식 투자를 할 경우 환규는 800 + 300 + 0 + 600 = 1700으로, 최대 1700의 이익을 남길 수 있다. N일 동안 A사, B사, C사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 모두 팔았을 경우의 손익을 정리한 데이터가 주어질 때, 환규가 N일간 규칙을 지키며 최적의 투자를 했을 경우 얻을 수 있었을 최대 이윤을 출력하는 프로그램을 작성하시오.

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫째 줄에는 테스트 케이스의 개수를 나타내는 자연수 T가 주어진다. 각각의 테스트 케이스의 첫째 줄에 환규가 정리한 주식 데이터의 일수를 나타내는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 N개의 줄에 각 회사별 주식을 구매했을 때, 그날 그날의 손익을 나타내는 3개의 정수 A, B, C (-1,000,000 ≤ A, B, C ≤1,000,000)가 주어진다. A는 A사의 주식을 구매했을 때의 손익, B는 B사의 주식을 구매했을 때의 손익, C는 C사의 주식을 구매했을 때의 손익을 나타낸다.

출력
출력은 표준 출력을 사용한다. 입력받은 데이터에 대해, 환규가 N일 동안 규칙을 지키며 최적의 투자를 했을 경우 얻을 수 있었을 최대 이익을 한 줄에 1개씩 출력한다.
"""

import sys

input = sys.stdin.readline

for T in range(int(input())):
    total = 0
    for N in range(int(input())):
        ABC = list(map(int, input().split()))

        if max(ABC) > 0:
            total += max(ABC)
    print(total)