"""지능형 기차2"""
maximum_people = 0
num_of_stops = 10
people = 0

for i in range(num_of_stops):
    out_, in_ = map(int, input().split())
    people += in_
    people -= out_

    if people > maximum_people:
        maximum_people = people
    else:
        pass

print(maximum_people)