"""
문제
현진 치킨에서 판매하는 치킨은 양념 치킨, 후라이드 치킨, 반반 치킨으로 총 세 종류이다. 반반 치킨은 절반은 양념 치킨, 절반은 후라이드 치킨으로 이루어져있다. 양념 치킨 한 마리의 가격은 A원, 후라이드 치킨 한 마리의 가격은 B원, 반반 치킨 한 마리의 가격은 C원이다.

상도는 오늘 파티를 위해 양념 치킨 최소 X마리, 후라이드 치킨 최소 Y마리를 구매하려고 한다. 반반 치킨을 두 마리 구입해 양념 치킨 하나와 후라이드 치킨 하나를 만드는 방법도 가능하다. 상도가 치킨을 구매하는 금액의 최솟값을 구해보자.

입력
첫째 줄에 다섯 정수 A, B, C, X, Y가 주어진다.

출력
양념 치킨 최소 X마리, 후라이드 치킨 최소 Y마리를 구매하는 비용의 최솟값을 출력한다.
"""

A, B, C, X, Y = map(int, input().split())

if A + B > 2 * C:
    half = min(X, Y)
    price = half * C * 2 + \
        min(2 * C, A) * max(0, X - half) + \
        min(2 * C, B) * max(0, Y - half)
else:
    price = A * X + B * Y

print(price)