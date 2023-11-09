"""심부름 가는 길"""
total = 0

for i in range(4):
    time = int(input())
    total += time

x, y = total // 60, total % 60
print(x)
print(y)