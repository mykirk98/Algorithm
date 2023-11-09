students = [i+1 for i in range(30)]

for i in range(28):
    attendance = int(input())
    students.remove(attendance)

result = " ".join(map(str, students))
print(result)