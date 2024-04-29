"""
문제
The UCF Programming Team coaches schedule practices regularly in fall and spring (by the way, all UCF students are welcome to the practices). During summer, the majority of the team members are gone but the coaches know how to make sure the students don’t get “rusty”. The coaches usually give prize money and reward the team members based on how many problems they solve during summer. For example, let’s assume the coaches have $1,000 in prize money and there are three students. Let’s also assume the three students solve, respectively, 5, 8 and 7 problems, i.e., a total of 20 problems. So, the reward for one problem will be $50 ($1000/20) and the three team members will receive, respectively, $250, $400 and $350.

Given the total prize money and the number of problems each team member has solved, compute the reward for each student.

입력
The first input line contains two integers: n (1 ≤ n ≤ 30), indicating the number of team members and d (1 ≤ d ≤ 30,000), indicating the dollar amount to be divided among the students. Each of the next n input lines contains an integer (between 1 and 300, inclusive) indicating the number of problems a team member has solved. Assume that the input values are such that the reward for one problem will be an integer number of dollars.

출력
Print the pay, in dollars, for each team member (in the same order as they appear in the input).
"""

n, d = map(int, input().split())

total_students = []
for i in range(n):
    total_students.append(int(input()))

for i in range(n):
    print(d * total_students[i] // sum(total_students))