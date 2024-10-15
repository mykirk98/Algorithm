"""
문제
7:00부터 19:00까지 전화 요금은 1분에 10원이다.

19:00부터 7:00까지 전화 요금은 1분에 5원이다.

상근이가 전화를 건 시간과 통화 시간이 모두 주어졌을 때, 전화 요금을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 건 전화의 수 N이 주어진다. (1 ≤ N ≤ 100)

다음 N개 줄에는 상근이가 건 전화에 대한 정보가 HH:MM DD와 같은 형식으로 주어진다.

HH:MM은 전화를 건 시간이며, DD는 통화 시간이다. DD는 최대 60이며, MM과 DD사이에는 공백이 하나 주어진다.

만약 시나 분이 한자리 숫자라면, 앞에 0이 하나 주어진다.

시간은 00:00부터 23:59까지이다.

출력
총 전화 요금을 출력한다.
"""

import sys

fee = 0
for N in range(int(sys.stdin.readline())):
    HH, rear = map(str, sys.stdin.readline().split(':'))
    MM, DD = rear.split()
    HH, MM, DD = int(HH), int(MM), int(DD)
    # MM, DD = MM.split()
    
    if 7 <= HH < 19:    # 분당 10원일 때
        if HH == 18 and MM + DD >= 60:      # 요금 변화시간대에 걸쳐있으면
            exceed = MM + DD - 60
            fee += 10 * (DD - exceed) + 5 * exceed
        else:                               # 걸쳐있지 않으면
            fee += 10 * DD
    else:               # 분당 5원일 때
        if HH == 6 and MM + DD >= 60:       # 요금 변화시간대에 걸쳐있으면
            exceed = MM + DD - 60
            fee += 5 * (DD - exceed) + 10 * exceed
        else:                               # 걸쳐있지 않으면
            fee += 5 * DD

print(fee)