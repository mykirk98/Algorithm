"""나는 요리사다"""
scores = []

for i in range(5):
    scores.append(sum(map(int, input().split())))

print(scores.index(max(scores)) + 1, max(scores))