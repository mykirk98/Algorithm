"""
문제
해빈이는 학교를 다니면서 틈틈히 번 돈으로 자동차를 사려고 한다.
자동차에 여러 가지 옵션을 포함시킬 수 있는데 해빈이는 덧셈과 곱셈을 하지 못하기 때문에 친구 태완이에게 도움을 청했다. 하지만 태완이도 덧셈과 곱셈을 못한다. 불쌍한 이 두 친구를 위해 모든 옵션이 주어진 자동차를 구매하는데 필요한 액수를 계산해 주자.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다.
각 테스트 케이스의 첫 줄엔 자동차의 가격 s가 주어진다. (1 ≤ s ≤ 100 000)
둘째 줄엔 해빈이가 구매하려고 하는 서로 다른 옵션의 개수 n이 주어진다. (0 ≤ n ≤ 1 000)
뒤이어 n개의 줄이 입력으로 들어온다.
각 줄은 q 와 p로 이루어져 있는데 q는 해빈이가 사려고 하는 특정 옵션의 개수이고 p는 해당 옵션의 가격이다. (1 ≤ q ≤ 100, 1 ≤ p ≤ 10 000)

출력
각 테스트 케이스 마다, 해빈이가 최종적으로 구매하려는 자동차의 가격을 한줄씩 출력한다.
"""

T = int(input())

for t in range(T):
    initial_price = int(input())

    number_of_options = int(input())

    total_price = 0
    total_price += initial_price

    for n in range(number_of_options):
        q, p = map(int, input().split())
        
        total_price += q * p

    print(total_price)