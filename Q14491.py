"""
문제
10진수를 9진수로 바꾸자.

컴파일러: 

입력
첫째 줄에 10진수 T(1 ≤ T ≤ 10,000)가 주어진다.

출력
T를 9진수로 변환한 수를 출력한다.
"""

T = int(input())

array = []
while T // 9 != 0:
    array.append(T % 9)
    T //= 9

array.append(T)

print(*array[::-1], sep='')