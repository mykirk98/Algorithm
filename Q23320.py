"""
문제
2021년, 홍익대학교는 절대평가를 시행한다. 착한 도현이는 A학점을 받는 사람이 최대한 많았으면 한다.

시험을 응시한 학생의 수 
$N$, 상대평가 시 A학점의 비율 
$X\%$와 절대평가 시 A학점을 받기 위한 최소 점수 
$Y$점이 주어질 때, 상대평가 시 A학점을 받는 인원의 수와 절대평가 시 A학점을 받는 인원의 수를 구하는 프로그램을 작성해보자.

입력
첫째 줄에 시험을 응시한 학생의 수 정수 
$N$ (
$10 \leq N \leq 100$, 
$N$은 
$10$의 배수) 이 주어진다.

둘째 줄에 길이가 
$N$인 정수 수열 
$A$ (
$1 \leq A_i \leq 100$)가 공백을 기준으로 주어진다. 
$i$번째로 주어지는 수 
$A_i$는 
$i$번째 학생의 점수이다. 모든 학생의 점수는 다르다.

셋째 줄에 상대평가 시 A학점의 비율 
$X$ (
$10 \leq X \leq 100$, 
$X$는 
$10$의 배수)와 절대평가 시 A학점을 받기 위한 최소 점수 
$Y$ (
$1 \leq Y \leq 100$)가 정수로 주어진다.

출력
첫째 줄에 상대평가 시 A학점을 받는 인원의 수와 절대평가 시 A학점을 받는 인원의 수를 공백으로 구분해 출력한다.
"""

N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

relative_score = len(A) * (X / 100)

absolute_score = 0
for a in A:
    if a >= Y:
        absolute_score += 1

print(round(relative_score), absolute_score)