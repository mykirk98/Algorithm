"""
문제
홍준이는 축구 경기를 보고 있다. 그러다가 홍준이는 역시 두 팀 중 적어도 한 팀이 골을 소수로 득점할 확률이 궁금해 졌다. 축구 경기는 90분동안 이루어지고, 분석을 쉽게하기 위해서 경기를 5분 간격으로 나눴다. 처음 간격은 처음 5분이고, 두 번째 간격은 그 다음 5분, 그리고 이런식으로 나눈다. 경기가 진행되는 동안 각 간격에서 A팀이 득점할 확률과 B팀이 득점할 확률이 주어진다. 그리고, 각 간격에서 두 팀은 각각 많아야 한 골을 득점할 수 있다. 경기가 끝난 후 적어도 한 팀이 골을 소수로 득점할 확률을 구하시오.

입력
첫째 줄에 A팀이 득점할 확률, 둘째 줄에 B팀이 득점할 확률이 퍼센트 단위로 주어진다. 퍼센트 단위로 주어지는 확률은 모두 0보다 크거나 같고 100보다 작거나 같은 정수이다.

출력
첫째 줄에 적어도 한 팀이 골을 소수로 득점할 확률을 출력한다. 정답과의 절대/상대 오차가 10-6이내인 경우에 정답이다.
"""

def combination(n, c):
    result = 1
    c = max(c, n - c)
    for e, i in enumerate(range(n, c, -1)):
        result *= i
        result /= (e + 1)
    
    return int(result)

A = int(input()) / 100
B = int(input()) / 100

non_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

A_prob, B_prob = [], []
for i in non_prime:
    A_prob.append(combination(n=18, c=i) * (A ** i) * ((1 - A) ** (18 - i)))
    B_prob.append(combination(n=18, c=i) * (B ** i) * ((1 - B) ** (18 - i)))

total_A = sum(A_prob)
total_B = sum(B_prob)

print(1 - total_A * total_B)