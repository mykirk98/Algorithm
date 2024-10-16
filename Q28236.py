"""
문제
송도고에서는 점심시간만 되면 밥을 일찍 먹으려는 학생들이 레이스를 펼친다.

학교 본관은 
$n$개의 층으로 이루어져 있으며 모든 층에는 계단, 
$m$개의 교실, 계단이 순서대로 배치되어 있다. 각 교실과 계단은 하나의 칸으로서 표현된다. 한 칸을 이동하는 데에는 
$1$분이 걸리고, 층간 이동은 계단을 통해서만 할 수 있다.

급식실은 
$1$층 맨 오른쪽 칸에서 오른쪽으로 나가면 있다.



레이싱이 이루어질 본관과 급식실의 모습이다.

송도고의 점심시간 레이스에는 총 
$k$개의 반이 참가하며, 각 반은 
$1$번부터 
$k$번까지의 번호로 구분된다. 
$i$번째 반이 점심시간 직전에 수업을 진행하는 교실의 위치는 
$f_i$층의 왼쪽 계단 칸으로부터 
$d_i$칸 떨어진 교실이다. 각 반의 학생들은 급식실과 연결된 문을 향해 항상 가장 빠른 경로로 움직인다. 급식실에 가장 먼저 도착하는 반이 레이스에서 우승한다. 단, 각 반의 위치는 겹칠 수 있음에 유의하라.

혼란에 빠진 송도고를 위해 점심시간 레이스에서 우승할 반을 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는  학교의 층수 
$n$, 한 층에 있는 교실의 수 
$m$, 레이스에 참가하는 반의 수 
$k$가 공백으로 구분되어 주어진다.

이어서 
$k$개의 각 
$i+1$번째 줄에 
$i$번째 반이 점심시간 직전에 수업을 진행하는 교실의 위치를 나타내는 정수 
$f_i$와 
$d_i$가 공백으로 구분되어 주어진다.

출력
점심시간 레이스에서 우승할 반의 번호를 출력한다.

공동 우승할 반이 존재한다면 공동 우승하는 반들 중 번호가 가장 작은 반의 번호를 출력한다.
"""

# import sys
# input = sys.stdin.readline

n, m, k = map(int, input().split())

possible = []
target = [1, m+1]

for cls, _ in enumerate(range(k)):
    coordi = list(map(int, input().split()))
    possible.append(abs(target[0] - coordi[0]) + abs(target[1] - coordi[1]))
    

print(possible.index(min(possible)) + 1)