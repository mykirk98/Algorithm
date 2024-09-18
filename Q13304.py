"""
문제
정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다. 여러 학년이 같은 장소로 수학여행을 가려고 하는데 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다. 1~2학년은 남학생, 여학생 구별 없이 방을 배정할 수 있으며 3~6학년은 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 또한 1~2학년은 학년 구별 없이 같은 방에 배정할 수 있으며 마찬가지로 3~4학년도, 5~6학년도 각각 학년 구별 없이 방을 배정할 수 있다. 물론 한 방에 한 명만 배정되는 것도 가능하다.

한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.

예를 들어, 수학여행을 가는 학생이 다음과 같다면 K = 2일 때 9개의 방이 필요하다. 

학년	여학생	남학생
1학년	영희	동호, 동진
2학년	혜진, 상희	경수
3학년	경희	동수, 상철, 칠복
4학년	 	달호
5학년	정숙	호동, 건우
6학년	수지	동건
입력
표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 한 방에 배정할 수 있는 최대 인원 수 K(1 ≤ K ≤ 1,000)가 공백으로 분리되어 주어진다. 다음 N 개의 각 줄에 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다. 성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다. 

출력
표준 출력으로 학생들을 모두 배정하기 위해 필요한 최소한의 방의 수를 출력한다. 
"""

# 1 & 2 학년은 남녀 구별 X, 학년 구별 X
# 3 & 4 학년은 남녀 구별 O, 학년 구별 X
# 5 & 6 학년은 남녀 구별 O, 학년 구별 X

students = [0, 0, 0, 0, 0]

N, K = map(int, input().split())

for n in range(N):
    S, Y = map(int, input().split())
    if Y in [1, 2]:
        students[0] += 1
    elif (Y in [3, 4]) and S == 0:
        students[1] += 1
    elif (Y in [3, 4]) and S == 1:
        students[2] += 1
    elif (Y in [5, 6]) and S == 0:
        students[3] += 1
    elif (Y in [5, 6]) and S == 1:
        students[4] += 1
    
rooms = 0
for c in students:
    if c % K == 0:
        rooms += c // K
    else:
        rooms += c // K + 1

print(rooms)

# print(students)