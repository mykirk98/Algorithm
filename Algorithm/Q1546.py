N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

scores_2 = []
for s in scores:
    scores_2.append(s / M * 100)

average = sum(scores_2) / N

print(average)