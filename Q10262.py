"""
문제
꿍과 석은 군대에서 수많은 보드게임을 해서 일반적으로 6개의 면을 갖는 주사위가 아닌 특이한 주사위들, 예를 들면, 47,48,...,56이 적혀있는 10개의 면을 가진 주사위 등을 갖고 있다.

할일없는 군대에서, 꿍과 석은 각자 갖고있는 2개의 주사위를 굴려서 합이 높은 사람이 이기는 새로운 주사위게임을 만들어보기로 했다.

모든 주사위는 숫자 a,a+1,...,b 가 각면에 적혀있는데 이때, a와 b는 그 주사위에서 가장 작은 숫자와 가장 큰 숫자를 나타낸다. 모든 숫자들은 각 면에 하나씩만 적혀있으므로 주사위는 b-a+1개의 면을 갖게되는 것이다.

꿍과 석의 주사위가 어떻게 생겼는지 주어졌을 때 누가 승률이 높을까?

입력
첫째 줄에 꿍의 주사위를 알려주는 네 개의 숫자, a1, b1, a2, b2 가 주어진다.

주사위는 각 면에 ai, ai+1, ... , bi 의 숫자들을 갖고 있고, 1 ≤ ai ≤ bi ≤ 100 이다.

주사위는 최소 4개의 면을 가질 것이므로 ai + 3 ≤ bi 임을 유추할 수 있다.

두 번째 줄에는 같은 방식으로 석의 주사위가 주어진다.

출력
승률이 더 높은 플레이어를 출력하면 된다.

꿍의 승률이 더 높으면 "Gunnar", 석의 승률이 더 높으면 "Emma"를 출력하고 두 명의 승률이 같을 경우, "Tie"를 출력한다.
"""

a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())

expectation = []
for a, b in zip([a1, a2, c1, c2], [b1, b2, d1, d2]):
    result = 0
    for i in range(a, b+1):
        result += i
    result /= (b - a + 1)
    expectation.append(result)

Gunnar = expectation[0] + expectation[1]
Emma = expectation[2] + expectation[3]

if Gunnar > Emma:
    print("Gunnar")
elif Gunnar < Emma:
    print("Emma")
else:
    print("Tie")