import math

T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 규현과 승환 사이의 거리

    if distance == 0 and r1 == r2:  # 두 원의 중심이 같고 r1과 r2가 같을 때
        print(-1)
    elif distance == (r1 + r2) or distance == abs(r1 - r2):  # 외접원 or 내접원 일 때
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):  # 원 두개가 만나서 점 2개일 때
        print(2)
    else:
        print(0)