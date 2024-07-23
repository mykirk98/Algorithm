"""
문제
2015, 2016, 2017년에 이어 올해도 연세대학교 컴퓨터과학과 프로그래밍 경진대회가 열린다.

도현이는 4년 연속 교내대회가 개최된다는 것에 감격하여, 사비를 털 각오로 화려한 개막식을 준비했다.

도현이가 원하는 것은 폭죽으로, 강의실 A528에서 천장을 다 뚫어버리며 터지는 화려한 폭죽을 모두가 좋아할 것이라 생각했다. 도현이는 아래와 같이 터지는 폭죽을 주문하려 한다.

처음 발사된 폭죽이 만든 하나의 대형 불꽃은 적당한 높이에 도달하면 화려한 폭발과 함께 K개의 중형 불꽃으로 갈라진다.
각 K개의 중형 불꽃은 다시 각각 K개의 소형 불꽃으로 갈라지며 터진다.
그 이후 모든 불꽃은 소멸한다.
도현이는 적당한 폭죽을 찾아보려 했지만, 폭죽 판매처에서는 K의 값을 알려주지 않았고,

대신 폭죽 하나당 만들어지는 총 불꽃의 수(처음 터진 대형 불꽃을 포함해, 중형 불꽃과 소형 불꽃을 모두 포함한 수)만을 알려줬다. 결국 도현이는 어떤 폭죽이 적당할지 알아내지 못해 폭죽을 구매하지 못했다.

이에 도현이는 이 난제를 해결해주는 학생에게 이번 대회에서 맞은 문제 수를 하나 늘려주기로 하였다. 여러분은 대회에서 우승하기 위해, 폭죽이 만들 모든 불꽃의 개수가 주어지면 K의 값을 찾아보도록 하자.

입력
총 불꽃의 수 N이 주어진다. (3 ≤ N ≤ 10101)

출력
K의 값을 출력한다. 이 값은 정수임이 보장되며, 불가능한 경우는 입력으로 주어지지 않는다.
"""

N = int(input())

K = 0
while True:
    K += 1
    if K ** 0 + K ** 1 + K ** 2 == N:
        print(K)
        break