"""
문제
컴퓨터는 뺄셈을 처리할 때 내부적으로 2의 보수를 사용한다. 어떤 수의 2의 보수는 해당하는 숫자의 모든 비트를 반전시킨 뒤, 1을 더해 만들 수 있다. 이때, 32비트 기준으로 처음 표현했던 수와 그 2의 보수의 서로 다른 비트 수를 출력하라. 

입력
첫째 줄에 정수 N(1 ≤ N ≤ 109)이 주어진다.

출력
첫째 줄에 N과 N의 보수의 서로 다른 비트 수를 출력한다.
"""

N = int(input())

bin_list = [0] * 32
for i in range(32-1, -1, -1):
    bin_list[i] = N % 2
    N //= 2

# print(bin_list)

reverse = []
for b in bin_list:
    reverse.append((b + 1) % 2)

parity_bit = 1
rev_parity = [0] * 32
for r in range(len(reverse)-1, -1, -1):
    rev_parity[r] = (reverse[r] + parity_bit) % 2
    parity_bit = (reverse[r] + parity_bit) // 2

# print(rev_parity)

counter = 0
for i in range(32):
    if bin_list[i] != rev_parity[i]:
        counter += 1

print(counter)