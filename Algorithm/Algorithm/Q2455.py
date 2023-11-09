total_people = 0

max = 0

for i in range(4):
    out_, in_ = map(int, input().split())

    total_people += in_

    total_people -= out_

    if total_people > max:
        max = total_people

print(max)