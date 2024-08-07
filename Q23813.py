"""
문제
정수 
$N$이 주어질 때, 
$N$의 일의 자리 숫자를 떼서 제일 앞자리 왼쪽에 이어 붙힌 것을 
$N$의 회전이라고 정의하자. 예를 들어, 12345의 회전은 51234가 된다. 3의 회전은 3이 된다. 이렇게 회전을 계속하다 보면 원래 
$N$으로 돌아오게 된다. 원래 
$N$으로 돌아올 때까지의 
$N$을 회전하여 나온 수를 모두 더한 값을 출력하시오.

입력
모든 자리의 숫자가 다른 정수 
$N$이 주어진다. 각 자리의 숫자는 1이상이고, 
$1 \leq N \leq 987,654,321$이다.

출력
 
$N$의 회전 결과들을 모두 더한 값을 출력한다. 단, 결과값을 32비트 정수형으로 처리할 수 없을 수 있음에 유의하라.
"""

N = input()

A_Z = 0
for n in N:
    A_Z += int(n)

total = 0
for i in range(len(N)):
    total += A_Z * 10 ** i

print(total)