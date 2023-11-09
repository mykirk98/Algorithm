"""직사각형에서 탈출"""
x, y, w, h = map(int, input().split())

minimum_x = min(x - 0, w - x)
minimum_y = min(y - 0, h - y)

if minimum_x < minimum_y:
    print(minimum_x)
else:
    print(minimum_y)