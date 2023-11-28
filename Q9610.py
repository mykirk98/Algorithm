"""
문제
2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다. 다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다. (-106 ≤ xi, yi ≤ 106)

출력
각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력한다.


"""

n = int(input())

Quarter = [0, 0, 0, 0, 0]

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:        # axis
        Quarter[0] += 1
    elif x > 0 and y > 0:       # 1st quarter
        Quarter[1] += 1
    elif x < 0 and y > 0:       # 2nd quarter
        Quarter[2] += 1
    elif x < 0 and y < 0:       # 3rd quarter
        Quarter[3] += 1
    elif x > 0 and y < 0:
        Quarter[4] += 1
    else:
        pass

print(f"Q1: {Quarter[1]}")
print(f"Q2: {Quarter[2]}")
print(f"Q3: {Quarter[3]}")
print(f"Q4: {Quarter[4]}")
print(f"AXIS: {Quarter[0]}")