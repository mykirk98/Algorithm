"""평균 점수"""
number_of_students = 5
scores = []
sum = 0

for i in range(number_of_students):
    scores.append(int(input()))

    if scores[i] >= 40:
        pass
    else:
        scores[i] = 40
    
    sum += scores[i]

average = int(sum / number_of_students)
print(average)