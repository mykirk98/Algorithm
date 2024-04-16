"""
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""


def factorial(N):
    if N > 1:   
        return N * factorial(N-1)
    else:
        return 1

N = int(input())

number = str(factorial(N))
counter = 0

for i in number[::-1]:
    if i == '0':
        counter += 1
    else:
        break

print(counter)