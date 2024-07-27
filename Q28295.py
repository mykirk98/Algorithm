"""
문제
UCPC 초등학교의 체육대회 날이 다가오고 있다. UCPC 초등학교 1학년 1반의 학생들은 담임 선생님 종서의 지시에 맞춰 특정한 방향을 바라보는 연습을 하고 있다.

학생들은 초기에 북쪽을 바라보고 있으며, 종서는 다음과 같은 형태의 지시를 총 열 번 내린다:

우향우: 각 학생은 현재 상태에서 오른쪽으로 
$90$도 돈다.
뒤로 돌아: 각 학생은 현재 상태에서 오른쪽으로 
$180$도 돈다.
좌향좌: 각 학생은 현재 상태에서 왼쪽으로 
$90$도 돈다.
종서는 초등학생들이 지시를 정확하게 이행하는 것이 어렵다는 것을 인지하고, 학생들이 자신의 지시를 성공적으로 따른다면 사탕을 나누어 주기로 했다. 학생들을 도와 담임 선생님 종서의 지시대로 바라보는 방향을 바꾸었을 때, 최종적으로 바라보는 방향을 구해보자.

입력
 
$10$개의 줄에 걸쳐 종서가 내린 각 지시에 대한 정보를 나타내는 정수 
$t_i(1\le i\le 10)$가 한 줄에 하나씩 주어진다. 
$t_i$의 값은 
$1$, 
$2$, 
$3$ 중 하나로,

 
$t_i=1$이라면 
$i$ 번째 명령이 우향우임을,
 
$t_i=2$라면 
$i$ 번째 명령이 뒤로 돌아임을,
 
$t_i=3$이라면 
$i$ 번째 명령이 좌향좌임을
나타낸다.

출력
 
$10$개의 지시를 모두 이행한 후 학생들이 바라보는 방향을 나타내는 문자를 출력한다. 학생들이 바라보는 방향이 북쪽이라면 N, 동쪽이라면 E, 서쪽이라면 W, 남쪽이라면 S를 출력한다.
"""
total = 0
for i in range(10):
    total += int(input())

total %= 4
if total == 0:
    print('N')
elif total == 1:
    print('E')
elif total == 2:
    print('S')
else:
    print('W')